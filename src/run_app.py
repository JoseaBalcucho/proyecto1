
import argparse
import sys
import time

sys.path.insert(1, '/Users/josebalcucho/bigdata/git/proyect1/src/utils/')
from files_process import Files_process
from data_process import Data_process


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Proceso que xxx.')
    parser.add_argument(
        '--id',
        help='Id Pelicula')
    parser.add_argument(
        '--date',
        help='Fecha a reprocesar')

    args = parser.parse_args()

    
    default_filename = "USERS_{date}"

    if args.id is  None:
        parser.print_help(sys.stderr)
        sys.exit(1)
    elif args.date is not None:
        filename = default_filename.format(date=args.date)
    else:
        date = time.strftime("%Y%m%d")
        print (date)
        filename = default_filename.format(date=date)

    file = Files_process()
    file.get_file(filename)

    data= Data_process()
    result = data.get_id(args.id)
    if(result is not None):
        file.write_file(result)

    

   

