from Empleado import Empleado as e

def main():
    employers = e.create_employers()
    e.file_write(employers)

if __name__ == '__main__':
    main()

