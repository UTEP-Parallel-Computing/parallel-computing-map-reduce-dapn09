'''
Title: WordCount
Author: Daniel Pacheco
Description: This script takes a set of files and a list of words, then looks for the occurrences of those words
            in the files listed. This is performed using paralelization (pymp).
'''

import pymp
import re

#Instead we will create handles to the files.
def openFiles(files=[]):
    handles = []
    for file in files:
        handles.append(open(file, "r"))
    return handles

def countInstances(target, file):
    total = 0
    wordsInFile = str(file.read()).lower()
    return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(str(target).lower()), wordsInFile))

def main(files, words):
    files = openFiles(files)
    wordCounts = pymp.shared.array((len(words),), dtype='int64')
    with pymp.Parallel(1) as p:
        for fIndex in p.range(0, len(files)):
            for wordIndex in range(0, len(words)):
                count = countInstances(words[wordIndex], files[fIndex])
                #p.lock.acquire()
                print(f"Thread {p.thread_num}, file \'{files[fIndex]}\', word \'{words[wordIndex]}\', count {count}")
                wordCounts[wordIndex] += count
                #p.lock.release()
    print(wordCounts)


if __name__ == "__main__":
    words = ["hate", "love", "death", "night", "sleep", "time", "henry", "hamlet", "you", "my", "blood", "poison", "macbeth", "king", "heart", "honest"]
    files = ["shakespeare1.txt", "shakespeare2.txt", "shakespeare3.txt", "shakespeare4.txt", "shakespeare5.txt", "shakespeare6.txt", "shakespeare7.txt", "shakespeare8.txt"]
    main(files, words)
