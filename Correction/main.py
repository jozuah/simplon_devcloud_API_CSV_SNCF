from classes2 import ReadSncfApi

def main():

    sncf = ReadSncfApi()
    sncf.read_json()
    sncf.read_links()
    sncf.save_csv()


if __name__ == 'main':
    main()