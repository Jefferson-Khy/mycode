#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        houses = []
        for url in got_dj["allegiances"]:
            house = requests.get(url).json()
            houses.append(house["name"])
        books = []
        for url in got_dj["books"]:
            book = requests.get(url).json()
            books.append(book["name"])

        print("\nKnown houses: ")
        pprint.pprint(houses)
        print("\nKnown books: ")
        pprint.pprint(books)

       # pprint.pprint('Known books: :', got_dj["books"])

if __name__ == "__main__":
        main()

