import sys
from typing import *


if __name__ == '__main__':
    import psycopg2

    conn = sys.argv[1]
    n_retries = int(sys.argv[2])

    # conn = "host=localhost port=5433 dbname=dcat user=dcat_user password=d393c705ea42"
    # n_retries = 10
    success = False
    print(f"Trying to connect to: `{conn}`: ", end="", flush=True)

    for _ in range(n_retries):
        try:
            conn = psycopg2.connect(conn, connect_timeout=2)
            conn.close()
            success = True
            break
        except psycopg2.OperationalError as ex:
            if str(ex).find('timeout expired') != -1:
                print(".", end="", flush=True)
            else:
                print("Connection failed: {0}".format(ex))
                exit(-1)

    if success:
        print("\nConnect successfully!")
        exit(0)
    else:
        print("\nCannot connect to Postgres")
        exit(-1)
