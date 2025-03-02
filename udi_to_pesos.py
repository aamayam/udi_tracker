import argparse
from tracker import UDITracker
from datetime import datetime as dt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('amount',type=float, help="El monto en UDIS a pagar")
    
    try:
        args = parser.parse_args()

        token = 'c9be2c44c1c6d8c9274235897f3989a390b8fdacc4f891656ca59f9e0622cf31'
        tracker = UDITracker(token)
        date = dt.now().strftime('%Y-%m-%d')
        valor_udi = float(tracker.get_udi_series(date).dato[0])

        print("El valor de la UDI al día " + date + " es: " + str(valor_udi))

        if args.amount:
            monto_a_pagar = valor_udi * args.amount 
            print("El total a pagar por " + str(args.amount) + " UDI's es de: $" + str(round(monto_a_pagar,ndigits=2)))
        
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

