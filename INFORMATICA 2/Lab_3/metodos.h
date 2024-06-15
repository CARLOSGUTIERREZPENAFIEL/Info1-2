#ifndef METODOS_H
#define METODOS_H

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

string leerArchivo(const string nombreArchivo, int identificador);
string convertir_a_binario(string contenido);
string* separar_en_bloques(string contenido_en_binario, int numero);
string* metodo_1(string* arreglo);
string* metodo_2(string* arreglo);
string* decodificacion_metodo_2(string* codificado, int cant_bloques);
string* decodificacion_metodo_1(string* codificado, int cant_bloques);
string** usuarios_totales(const string nombreArchivo);
bool comprobarClave(string clave, string* clave_codificada, int cant_bloques);
int cantidad_usuarios(const string nombreArchivo);
void aumentarTamano(string**& usuarios, int& cant_us);
void actualizar_datos(string** nuevoUsuarios, int cant_usuarios);
string* cambio_separar_bloques(string* separado, int cantidad_bloques);
string convertir_a_texto(string* arreglo, int dimension);

void eliminar_datos();
#endif // METODOS_H
