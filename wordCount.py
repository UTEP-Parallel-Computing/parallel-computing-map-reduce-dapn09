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
    texts = []

    for file in files:
        texts.append(file.read())

    wordCounts = pymp.shared.dict()

    with pymp.Parallel(numThreads) as p:
        for word in words:
            wordCounts[word] = 0
        for text in p.iterate(texts):
            for word in words:
                count = countInstances(word, text)
                p.lock.acquire()
                wordCounts[word] = wordCounts[word] + count
                p.lock.release()
    return wordCounts

def main():
    words = ["love", "hate", "death", "night", "sleep", "time", "henry", "hamlet", "you", "my", "blood", "poison", "macbeth", "king", "heart", "honest"]
    files = ["shakespeare1.txt", "shakespeare2.txt", "shakespeare3.txt", "shakespeare4.txt", "shakespeare5.txt", "shakespeare6.txt", "shakespeare7.txt", "shakespeare8.txt"]

    print("Count totals...")
    print("\nWord\tAppearances\n")

    #Opening files
    startTime = time.time()
    docs = openFiles(files)
    openFilesTime = time.time() - startTime

    startTime = time.time()
    totals = findCountsParallel(docs, words, numThreads=4)
    countingTime = time.time() - startTime

    for word, count in totals.items():
        print(f"{word}\t{count}")

    print("\nTesting with more cores...\n")
    for i in range(0, 10, 2):
        results = 0
        startTime = time.time()
        if i == 0:
            results = findCountsParallel(docs, words, numThreads=1)
            print(f"1 thread execution time: {time.time() - startTime}")
        else:
            results = findCountsParallel(docs, words, numThreads=i)
            print(f"{i} threads execution time: {time.time() - startTime}")

    print("\nDisplaying runtimes...\n")
    print(f"Time spent opening files: {openFilesTime}")
    print(f"Time spent counting words: {countingTime}\n")

if __name__ == "__main__":
    main()
