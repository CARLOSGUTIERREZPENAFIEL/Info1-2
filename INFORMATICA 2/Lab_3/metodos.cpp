#include "metodos.h"
#include <iostream>
#include <string>
#include <fstream>
using namespace std;
string convertir_a_texto(string* arreglo, int tamanio) {
    string* arreglo_8_bits = new string[tamanio / 2];
    string aux;
    int contador = 0;

    // Convertimos los dígitos binarios de 4 en 4 y los almacenamos en arreglo_8_bits
    for (int i = 0; i < tamanio; i++) {
        aux += arreglo[i];
        contador += 1;
        if (contador == 2) {
            arreglo_8_bits[i / 2] = aux;
            aux.clear();  // Limpiamos aux para los próximos dígitos
            contador = 0;
        }
    }

    string texto;

    // Recorremos los elementos de arreglo_8_bits para convertirlos en caracteres ASCII
    for (int i = 0; i < tamanio / 2; i++) {
        char letra = 0;
        string codificado = arreglo_8_bits[i];

        // Convertimos los 8 bits en un byte
        for (int j = 0; j < 8; j++) {
            letra <<= 1;
            letra |= codificado[j] - '0'; // Convertimos el bit a su valor entero
        }
        texto.push_back(letra);
    }

    delete[] arreglo_8_bits;
    return texto;
}

bool comprobarClave(string clave, string* clave_codificada, int cant_bloques){
    string clave_codificada_unida;
    for(int i=0;i<cant_bloques;i++){
        clave_codificada_unida=clave_codificada_unida+clave_codificada[i];
    }
    while (!clave.empty() && (clave.back() == '\n' || clave.back() == '\r')) {
        clave.pop_back();
    }
    while (!clave_codificada_unida.empty() && (clave_codificada_unida.back() == '\n' || clave_codificada_unida.back() == '\r')) {
        clave_codificada_unida.pop_back();
    }

    if(clave==clave_codificada_unida){
        return true;
    }
    else{
        return false;
    }
}

void eliminar_datos() {
    ifstream inputFile("archivo.txt"); // Abre el archivo para leer
    string linea_correcta;

    if (!inputFile) {
        cerr << "No se pudo abrir el archivo." << endl;
        return;
    }

    string line;
    while (getline(inputFile, line)) { // Lee el archivo línea por línea
        size_t found = line.find(">"); // Busca el caracter ">"

        if (found == string::npos) { // Si no encuentra ">", actualiza la línea correcta
            linea_correcta = line;
        }
    }
    inputFile.close(); // Cerrar archivo de entrada

    ofstream archivo("archivo.txt", ofstream::out | ofstream::trunc); // Abre el archivo para escribir

    if (archivo.is_open()) {
        archivo << linea_correcta << endl;
        archivo.close(); // Cerrar archivo de salida
    } else {
        cerr << "No se pudo abrir el archivo." << endl;
    }

}


void actualizar_datos(string** nuevoUsuarios, int cant_usuarios) {


    // Abrir el archivo de salida en modo append (para agregar al final del archivo)
    ofstream archivo_salida("archivo.txt", ios::app);
    if (!archivo_salida.is_open()) {
        cerr << "Error al abrir el archivo de salida." << endl;
        return;
    }

    // Escribir los nuevos datos en el archivo línea por línea
    for (int i = 0; i < cant_usuarios; ++i) {
        archivo_salida << ">"; // Agregar el carácter '>' al comienzo de la línea
        for (int j = 0; j < 3; ++j) { // Aquí usamos directamente el tamaño 3
            archivo_salida << nuevoUsuarios[i][j];
            if (j < 2) { // Si no es el último elemento del arreglo, agregar una coma
                archivo_salida << ",";
            }
        }
        archivo_salida << endl; // Agregar salto de línea después de cada arreglo de strings
    }

    archivo_salida.close();
}



int cantidad_usuarios(const string nombreArchivo){
    ifstream archivo(nombreArchivo);

    char caracter;
    int signos = 0;

    while (archivo.get(caracter)) {
        if (caracter == '>') {
            signos++;
        }
    }
    return signos;
}

void aumentarTamano(string**& usuarios, int& cant_us) {
    // Aumentar el tamaño del arreglo dinámico
    int nuevoTamano = cant_us + 1;
    string** nuevoUsuarios = new string*[nuevoTamano];

    // Copiar datos existentes al nuevo arreglo
    for (int i = 0; i < cant_us; ++i) {
        nuevoUsuarios[i] = new string[3];
        for (int j = 0; j < 3; ++j) {
            nuevoUsuarios[i][j] = usuarios[i][j];
        }
    }

    // Liberar memoria del arreglo original
    for (int i = 0; i < cant_us; ++i) {
        delete[] usuarios[i];
    }
    delete[] usuarios;
    // Agregar el nuevo elemento vacío al final del nuevo arreglo
    nuevoUsuarios[nuevoTamano - 1] = new string[3]; // Crear un nuevo elemento vacío

    // Actualizar el puntero de usuarios y el tamaño
    usuarios = nuevoUsuarios;
    cant_us = nuevoTamano;
}

string** usuarios_totales(const string nombreArchivo){

    ifstream archivo(nombreArchivo);
    int signos = cantidad_usuarios(nombreArchivo);
    string** usuarios = new string*[signos]; // se guarda cada usuario con cada dato
        for (int i = 0; i < signos; ++i) {
        usuarios[i] = new string[3];
    }
    archivo.clear(); // Limpiar cualquier indicador de error
    archivo.seekg(0, std::ios::beg); // Mover el puntero al inicio del archivo
    string linea;
    int contador = 0;
    while (getline(archivo, linea)) {
        if (linea.empty() || linea[0] != '>') {
            continue; // Ignorar líneas que no comienzan con '>'
        }

        // Eliminar el primer carácter '>'
        linea = linea.substr(1);// se guarda cada linea  sin los parentesis angulares
        // Buscar las tres palabras separadas por comas
        size_t pos1 = linea.find(',');
        size_t pos2 = linea.find(',', pos1 + 1);



        if (pos1 != string::npos && pos2 != string::npos) {
            usuarios[contador] = new string[3];
            usuarios[contador][0] = linea.substr(0, pos1);
            usuarios[contador][1] = linea.substr(pos1 + 1, pos2 - pos1 - 1);
            usuarios[contador][2] = linea.substr(pos2 + 1);
            contador++;
        }
    }


    // Liberar la memoria asignada

    archivo.close();
    return usuarios;

}








string leerArchivo(const string nombreArchivo, int identificador){
    string contenido;
    string linea;
    ifstream archivo(nombreArchivo);
    if (!archivo.is_open()) { // Verificar si el archivo no se pudo abrir
        cout << "No se pudo abrir el archivo " << nombreArchivo << endl;
        return ""; // Devuelve una cadena vacía si no se pudo abrir el archivo
    }

    getline(archivo, linea);
    if(identificador==1){
        // Encontrar la posición del '<'
        size_t pos = linea.find('<');
        if (pos != string::npos) {
            // Extraer el valor después del '<'
            string valor = linea.substr(pos + 1);
    
            // Imprimir el valor
            return valor;
        }
    }
    while (getline(archivo, linea)) {
        contenido.append(linea);
        contenido.push_back('\n');
    }

    archivo.close();
    return contenido;
}

string convertir_a_binario(string contenido){
    string contenido_limpio;
    for (char caracter : contenido) {
        if (caracter != '\n' && caracter != '\r') {
            contenido_limpio = contenido_limpio + caracter;
        }
    }

    string contenido_en_binario;
    for (char caracter : contenido_limpio) {
        for (int i = 7; i >= 0; i=i-1) {
            if (caracter & (1 << i))
                contenido_en_binario= contenido_en_binario +'1';
            else
                contenido_en_binario= contenido_en_binario + '0';
        }
    }
    return contenido_en_binario;

}


string* separar_en_bloques(string contenido_en_binario, int numero){
    string x; //x almacena bloque por bloque
    int contador=1;
    int contador_de_ceros=0;
    int tamanio=contenido_en_binario.length();

    int contador_dos=1;
    while(tamanio%numero!=0){
        tamanio=tamanio+1;
        contador_de_ceros=contador_de_ceros+1;
    }
    int cantidad_bloques=tamanio/numero;
    string* arreglo=new string[cantidad_bloques+1];
    arreglo[0] = to_string(cantidad_bloques);


    while(contador_de_ceros>0){
        contenido_en_binario=contenido_en_binario+'0';
        contador_de_ceros=contador_de_ceros-1;
    }
    for (int i = 0; i < tamanio; i=i+1) {

        char digito = contenido_en_binario[i];
        x=x+digito;
        if(contador==numero){
            arreglo[contador_dos]=x;
            contador_dos=contador_dos+1;//contador de las posiciones del arreglo
            x.clear();
            contador=0;
        }
        contador=contador+1;
    }
    return arreglo;
}



string* metodo_1(string* arreglo){

    string primer_bloque = arreglo[1]; //se está guardando el bloque 1 sin codificar
    int contador_met_1=1;
    int cantidad_bloques=stoi(arreglo[0]); // se está pasando de string a entero
    int dim_bloques=primer_bloque.length(); //dim de cada bloque
    string bloque_codificado;// se guardan todos los bloques codificados de manera temporal
    string* arreglo_codificado = new string[cantidad_bloques];

    for (int i = 0; i < dim_bloques; i = i + 1) {
        char contador = primer_bloque[i];
        if (contador == '1') {
            bloque_codificado=bloque_codificado+'0';
        }
        else if (contador == '0') {
            bloque_codificado = bloque_codificado+'1';
        }
    }
    arreglo_codificado[0]=bloque_codificado;// se guarda el bloque 1 codificado
    bloque_codificado.clear();// se LIMPIA, para ir guardando los bloques codificados

    int contador=2;
    string bloque_A=primer_bloque;// sin codificar
    string bloque_B=arreglo[contador];

    while(contador<=cantidad_bloques){ //se repite hasta que contador = a la cantidad de bloques
        int unos=0;
        int ceros=0;
        int contador_caso_dos=1;
        int contador_caso_tres=2;
        for (int i = 0; i <dim_bloques; i=i+1){
            char caracter = bloque_A[i];
            if (caracter == '1') {
                unos=unos+1; //cantidad de 1 en el primer bloque
            } else if (caracter == '0') {
                ceros=ceros+1; //cantidad de 0 en el primer bloque
            }
        }


        if(ceros==unos){ // 1er caso
            for(int i=0; i<dim_bloques; i=i+1){
                char contador = bloque_B[i];
                if (contador == '1') {
                    bloque_codificado = bloque_codificado+'0';
                }
                else if (contador == '0') {
                    bloque_codificado = bloque_codificado+'1';
                }
            }
        }
        else if(ceros>unos){ //2do caso
            bloque_codificado=bloque_B;
            while(contador_caso_dos<dim_bloques){
                char contador = bloque_B[contador_caso_dos];
                if (contador == '1') {
                    bloque_codificado[contador_caso_dos] = '0';
                }
                else if (contador == '0') {
                    bloque_codificado[contador_caso_dos] = '1';
                }

                contador_caso_dos=contador_caso_dos+2;

            }
        }
        else if(unos>ceros){ // tercer caso
            bloque_codificado=bloque_B;
            while(contador_caso_tres<dim_bloques){
                char contador = bloque_B[contador_caso_tres];
                if (contador == '1') {
                    bloque_codificado[contador_caso_tres] = '0';
                }
                else if (contador == '0') {
                    bloque_codificado[contador_caso_tres] = '1';
                }

                contador_caso_tres=contador_caso_tres+3;
            }
        }
        arreglo_codificado[contador_met_1]=bloque_codificado;
        if(contador==cantidad_bloques){
            break;
        }
        bloque_codificado.clear();
        contador_met_1=contador_met_1+1;
        bloque_A.clear();
        bloque_A=bloque_B;
        bloque_B.clear();
        contador=contador+1;
        bloque_B=arreglo[contador];



    }

    return arreglo_codificado;
}


string* metodo_2(string* arreglo){

    int contador=1;
    int cantidad_bloques=stoi(arreglo[0]); // se está pasando de string a entero
    int dim_bloques=((arreglo[1]).length())-1; //dim de cada bloque
    string bloque_codificado;// se guardan todos los bloques codificados de manera temporal
    string* arreglo_codificado = new string[cantidad_bloques];


    while(contador<=cantidad_bloques){ //se repite hasta que contador = a la cantidad de bloques
        string bloque = arreglo[contador];
        bloque_codificado = bloque_codificado + bloque.back();
        bloque.erase(dim_bloques,1);
        bloque_codificado = bloque_codificado+bloque;
        arreglo_codificado[contador-1]=bloque_codificado;
        bloque.clear();
        bloque_codificado.clear();
        contador=contador+1;

    }

    return arreglo_codificado;
}

string* decodificacion_metodo_2(string* codificado, int cant_bloques){
    int contador=0;
    string* arreglo_decodificado = new string[cant_bloques];
    while(contador<cant_bloques){ //se repite hasta que contador = a la cantidad de bloques
        string bloque_codificado = codificado[contador];
        char primer_numero = bloque_codificado.front();
        bloque_codificado.erase(0,1);
        bloque_codificado=bloque_codificado+primer_numero;
        arreglo_decodificado[contador]=bloque_codificado;
        contador=contador+1;
        bloque_codificado.clear();
    }

    return arreglo_decodificado;
}

string* cambio_separar_bloques(string* separado, int cantidad_bloques){
    string* separado_cambiado = new string[cantidad_bloques];
    for(int i=1;i<=cantidad_bloques;i++){
        separado_cambiado[i-1]=separado[i];
    }
    return separado_cambiado;
}

string* decodificacion_metodo_1(string* codificado, int cantidad_bloques){

    string primer_bloque = codificado[0]; //se está guardando el bloque 1 sin codificar
    int contador_met_1=1;
    int dim_bloques=primer_bloque.length(); //dim de cada bloque
    string bloque_decodificado;// se guardan todos los bloques decodificados de manera temporal
    string* arreglo_decodificado = new string[cantidad_bloques];
    for (int i = 0; i < dim_bloques; i = i + 1) {
        char contador = primer_bloque[i];
        if (contador == '1') {
            bloque_decodificado=bloque_decodificado+'0';
        }
        else if (contador == '0') {
            bloque_decodificado = bloque_decodificado+'1';
        }
    }

    arreglo_decodificado[0]=bloque_decodificado;// se guarda el bloque 1 decodificado
    int contador=1;
    string bloque_A=bloque_decodificado;// sin codificar
    string bloque_B=codificado[contador];
    bloque_decodificado.clear();
    while(contador<cantidad_bloques){ //se repite hasta que contador = a la cantidad de bloques
        int unos=0;
        int ceros=0;
        int contador_caso_dos=1;
        int contador_caso_tres=2;

        for (int i = 0; i <dim_bloques; i=i+1){
            char caracter = bloque_A[i];
            if (caracter == '1') {
                unos=unos+1; //cantidad de 1 en el primer bloque
            } else if (caracter == '0') {
                ceros=ceros+1; //cantidad de 0 en el primer bloque
            }
        }

        if(ceros==unos){ // 1er caso
            for(int i=0; i<dim_bloques; i=i+1){
                char contador = bloque_B[i];
                if (contador == '1') {
                    bloque_decodificado = bloque_decodificado+'0';
                }
                else if (contador == '0') {
                    bloque_decodificado = bloque_decodificado+'1';
                }
            }
        }
        else if(ceros>unos){ //2do caso
            bloque_decodificado=bloque_B;
            while(contador_caso_dos<dim_bloques){
                char contador = bloque_B[contador_caso_dos];
                if (contador == '1') {
                    bloque_decodificado[contador_caso_dos] = '0';
                }
                else if (contador == '0') {
                    bloque_decodificado[contador_caso_dos] = '1';
                }

                contador_caso_dos=contador_caso_dos+2;

            }
        }
        else if(unos>ceros){ // tercer caso
            bloque_decodificado=bloque_B;
            while(contador_caso_tres<dim_bloques){
                char contador = bloque_B[contador_caso_tres];
                if (contador == '1') {
                    bloque_decodificado[contador_caso_tres] = '0';
                }
                else if (contador == '0') {
                    bloque_decodificado[contador_caso_tres] = '1';
                }

                contador_caso_tres=contador_caso_tres+3;
            }
        }

        arreglo_decodificado[contador_met_1]=bloque_decodificado;
        if(contador==cantidad_bloques-1){
            break;
        }
        bloque_A.clear();
        bloque_A=bloque_decodificado;
        bloque_decodificado.clear();
        contador_met_1=contador_met_1+1;
        bloque_B.clear();
        contador=contador+1;
        bloque_B=codificado[contador];



    }

    return arreglo_decodificado;
}







