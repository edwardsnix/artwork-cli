from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import requests
import sys

console = Console()


def main() -> None:
    # Title
    console.print(Panel("Artwork - Album Art Downloader v1.0"))
    # Get search query from user
    console.print(" Search <q to quit>: ", end="")
    search_query = input().strip()
    if search_query == "q":
        sys.exit()
    # Get list of results from API based on query
    try:
        results = search_api(search_query)
    except:
        sys.exit()
    # Generate Table from Results
    table = Table(title="Results Found")
    table.add_column("#", justify="center")
    table.add_column("Artist", justify="center")
    table.add_column("Album", justify="center")
    for index, result in enumerate(results):
        table.add_row(f"{index + 1}", result[0], result[1])
    console.print(table)
    # Get download selection
    while True:
        try:
            console.print(" Selection <q to quit>: ", end="")
            selection = input().strip()
            if selection == "q":
                sys.exit()
            selection = int(selection)
            if not (1 <= selection <= len(results)):
                continue
            break
        except (ValueError, TypeError):
            continue
    # Get file to save to/as from user
    console.print(" Save to/as: ", end="")
    file_name = input().strip()
    # Download artwork and print relevant success and unsuccessful message
    if download(results[selection - 1][2], file_name):
        console.print(" File successfully downloaded.")
    else:
        console.print(" File download unsuccesful")


def search_api(query: str) -> list:
    """
    Searches the iTunes API based on a query. Returns list of dicts 'results'.
    Raises HTTPError if response status code is not 200. Raises ValueError if no results found.

    :param query: Search Query to look for albums with API
    :type query: str
    :rtype: list
    :return: A list of results "dicts' with artistName, collectionName, and artworkUrl100
    """
    # Generate an iTunes API URL based on the query from the user. Request a response based on URL
    api_url = "https://itunes.apple.com/search?entity=album&term=" + query
    response = requests.get(api_url)

    if response.status_code == 200:
        # SUCCESSFUL REQUEST
        # Turn data to JSON and JSON to a list of results
        response_data = response.json()
        results = response_data["results"]
        # If there are no results based on query, raise an Exception
        if len(results) < 1:
            raise ValueError("No results found.")
        # Return a list of results from query
        return [
            (
                result["artistName"],
                result["collectionName"],
                result["artworkUrl100"].replace("100x100bb", "100000x100000-999"),
            )
            for result in results
        ]
    else:
        # UNSUCCESSFUL REQUEST
        raise requests.HTTPError()


def download(url: str, file_name: str) -> bool:
    """
    Downloads a URL passed, save to file name specified.
    Return True if successful, False if not

    :param url: Search Query to look for albums with API
    :type url: str
    :param file_name: Search Query to look for albums with API
    :type file_name: str
    :rtype: bool
    :return: Boolean if operation/download is successful
    """
    # Request a response from iTunes API to download the Artwork
    response = requests.get(url, allow_redirects=True)
    # If something went wrong, return False
    if response.status_code != 200:
        return False
    # Write the file to the specified file_name, return True if successful
    try:
        with open(file_name + ".jpg", "wb") as file:
            file.write(response.content)
    except PermissionError:
        sys.exit(
            " Something went wrong. Either directory is typed in or you don't have permission."
        )
    except FileNotFoundError:
        sys.exit(" Directory specified does not exist. Create it first and try again.")
    return True


if __name__ == "__main__":
    main()
