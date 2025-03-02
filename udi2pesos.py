import argparse
from tracker import UDITracker
from datetime import datetime as dt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--fecha','-f',type=str,help="fecha para obtener el valor de la UDI")
    parser.add_argument('monto',type=float, help="El monto en UDIs a pagar")
    
    try:
        args = parser.parse_args()

        token = 'c9be2c44c1c6d8c9274235897f3989a390b8fdacc4f891656ca59f9e0622cf31'
        tracker = UDITracker(token)

        if args.fecha:
            try:
                dt_obj = dt.strptime(args.fecha,'%Y-%m-%d')
                date = args.fecha
            except Exception as e:
                print("Error: El formato de fecha debe ser YYYY-MM-DD")
        else:
            date = dt.now().strftime('%Y-%m-%d')

        valor_udi = float(tracker.get_udi_series(date).dato[0])

        print("El valor de la UDI el dia " + date + " es: " + str(valor_udi))

        monto_a_pagar = valor_udi * args.monto
        print("El total a pagar por " + str(args.monto) + " UDI's es de: $" + str(round(monto_a_pagar,ndigits=2)))
        
        return 0
    except argparse.ArgumentTypeError:
        print("Error: El valor proporcionado no es un número decimal válido")
        return 1
    except Exception as e:
        print(f"Error inesperado: {str(e)}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)

