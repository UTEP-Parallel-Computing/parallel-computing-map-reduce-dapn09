'''
Title: WordCount
Author: Daniel Pacheco
Description: This script takes a set of files and a list of words, then looks for the occurrences of those words
            in the files listed. This is performed using paralelization (pymp).
'''

import pymp
import re
import time

#Instead we will create handles to the files.
def openFiles(files=[]):
    handles = []
    for file in files:
        handles.append(open(file, "r"))
    return handles

def countInstances(target, text):
    return sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(str(target).lower()), text))

def findCountsParallel(files, words, numThreads=1):
    files = openFiles(files)
    wordCounts = pymp.shared.dict()

    #Initialize dictionary
    for word in words:
        wordCounts[word] = 0

    with pymp.Parallel(numThreads) as p:
        for fIndex in p.range(0, len(files)):
            text = files[fIndex].read()
            for word in words:
                count = countInstances(word, text)
                p.lock.acquire()
                wordCounts[word] = wordCounts[word] + count
                p.lock.release()
    return wordCounts

def main():
    words = ["love", "hate", "death", "night", "sleep", "time", "henry", "hamlet", "you", "my", "blood", "poison", "macbeth", "king", "heart", "honest"]
    files = ["shakespeare1.txt", "shakespeare2.txt", "shakespeare3.txt", "shakespeare4.txt", "shakespeare5.txt", "shakespeare6.txt", "shakespeare7.txt", "shakespeare8.txt"]
    print(findCountsParallel(files, words, numThreads=4))

    for i in range(0, 10, 2):
        results = 0
        startTime = time.time()
        if i == 0:
            results = findCountsParallel(files, words, numThreads=1)
            print(f"Single thread execution time: {time.time() - startTime}")
        else:
            results = findCountsParallel(files, words, numThreads=i)
            print(f"{i} threads execution time: {time.time() - startTime}")

if __name__ == "__main__":
    main()
