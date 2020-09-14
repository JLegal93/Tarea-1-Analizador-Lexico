def readfile():
    input_file = open("fuente.txt", "r")
    output_file = open("output_file.txt", "w")
    mislexemas = \
        {
            '{': 'L_LLAVE',
            '}': 'R_LLAVE',
            '[': 'L_CORCHETE',
            ']': 'R_CORCHETE',
            ':': 'DOS_PUNTOS',
            ',': 'COMA',
            'str': 'STRING',
            'num': 'NUMBER',
            'FALSE': 'PR_FALSE',
            'TRUE': 'PR_TRUE',
            '\n': '\n',
        }
    aux_string = ''
    quote_count = 0
    line_count = 0
    number_count = 0
    for line in input_file:
        line_count += 1
        for lex in line:
            token = mislexemas.get(lex)
            if lex == '"':
                quote_count += 1
            if lex.strip().upper().startswith('F') or lex.strip().upper().startswith('T'):
                aux_string += lex
            else:
                aux_string = ''

            if token is not None:
                output_file.write(mislexemas.get(lex) + ' ')
                aux_string = ''
                number_count = 0

            elif lex.isalnum() or quote_count > 0:

                if quote_count == 2:
                    quote_count = 0
                    output_file.write(mislexemas.get('str') + ' ')
                elif quote_count == 0:
                    if lex.isnumeric() and number_count < 1:
                        output_file.write(mislexemas.get('num') + ' ')
                        number_count += 1
                    elif len(aux_string) > 3:
                        token = mislexemas.get(aux_string.strip().upper())
                        if token is not None:
                            output_file.write(token + ' ')
                            aux_string = ''
                            number_count = 0
            elif not lex.isspace() and len(aux_string) < 1:
                print(f"Lexema no reconocido linea:{line_count}")
    print("Proceso concluido... se genera el archivo 'output_file.txt' en el mismo directorio que el programa.")
    input_file.close()
    output_file.close()



def main():
    readfile()


if __name__ == '__main__':
    main()
