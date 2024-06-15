#ifndef CLASES_H
#define CLASES_H

#include<string>
#include<map>
#include<vector>


using namespace std;

void crearRouter();

void menuRouters();

void menuPrincipal();

void menuRed();

class Routers
{
private:
    string namePadreR;

    map<string, vector<pair<string, int>>>tablaEnrutamiento;//clave nombre de router vecino, primera poscicon de vector nombre del router padre , segunda posicion de vector costo de vecino

public:
    Routers(string nameRou);

    void agregarEnrutador();

    void eliminarEnrutador();

    void cambiarCosto();

    void dijkstra();

    void mostrarTablaEnrutamiento();
};










//----------------------------------------------------------------------------------------------------------------------------------------------------
class Red
{

private:

public:
    Red();

};

#endif // CLASES_H
//--------------------------------------------------------------------------------------------------------------------------------------------------


