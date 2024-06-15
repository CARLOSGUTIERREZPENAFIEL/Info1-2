#include "clases.h"

#include<iostream>
#include<string>
#include<map>
#include<vector>

using namespace std;



//---------------------------------------------------------------------------------------------------------------------------------------------------
Routers::Routers(string namePadreR)
{

    tablaEnrutamiento[namePadreR] = {{namePadreR, 0}};

}

void Routers::agregarEnrutador()
{   string nombreVecino;
    int costoDeRouter;
    cout<<"Ingresa el Nombre del enrutador: ";
    cin>>nombreVecino;
    cout<<"Ingresa el nuevo coste: ";
    cin>>costoDeRouter;
    tablaEnrutamiento.insert({nombreVecino, {{namePadreR, costoDeRouter}}});
    cout<<"\n";
    cout<<"Proceso exitoso."<<endl;
    menuRouters();

}

void Routers::eliminarEnrutador(){
    string nombreVecino;

    cout<<"Ingresa el Nombre del enrutador al cual se le va cambiar el precio de enlace: ";
    cin>>nombreVecino;

    //importante !!!!!verifica si el nombre del router si esta en el mapa!!!! si no esta devolver al menu principal de router

    tablaEnrutamiento.erase(nombreVecino);
    cout<<"\n";
    cout<<"Proceso exitoso."<<endl;
    menuRouters();
}




void Routers::cambiarCosto()
{
    string  nombreVecino;
    int nuevoCosto;
    cout<<"Ingresa el Nombre del enrutador al cual se le va cambiar el precio de enlace: ";
    cin>>nombreVecino;
    cout<<"Ingresa el nuevo coste: ";
    cin>>nuevoCosto;

    //importante !!!!!verifica si el nombre del router si esta en el mapa!!!! si no esta devolver al menu principal de router

    tablaEnrutamiento.insert({nombreVecino, {{namePadreR, nuevoCosto}}});
    cout<<"\n";
    cout<<"Proceso exitoso."<<endl;
    menuRouters();
}



void Routers::dijkstra()
{

}

void Routers::mostrarTablaEnrutamiento()
{
    cout << endl << endl << "*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/" << endl;
    cout << "**Tabla de Enrutamiento para el enrutador**" << namePadreR << endl;

    for (const auto& entry : tablaEnrutamiento) {
        cout << "Enrutador: " << entry.first << " | Vecino: " << entry.second[0].first << " | Costo: " << entry.second[0].second << endl;
    }
    cout << "*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/" << endl;
    menuRouters();

}








//-----------------------------------------------------------------------------------------------------------------------------------------------------------------


//-------------------------------------------------------------------------------------------------------------------------------------------------------

void menuRed()
{
    string opcion;
    cout<<"Bienvenido a menu de Red"<<endl;

    if(opcion=="1"){

    }
    else if(opcion=="2"){

    }
    else{
        menuPrincipal();

    }

}

void menuRouters()
{
    Routers routerA("A");

    string opcion;
    cout<< endl << "Bienvenido a menu de routers"<<endl;
    cout<<"1. Agregar enrutador en la red." << endl << "2. Eliminar enrutador de la red." << endl << "3. Cambiar el costo de alguna conexion." << endl << "*Ingrese cualquier otro numero para salir del sistema.*" << endl << "Opcion: ";
    cin>>opcion;

    if(opcion=="1"){

        routerA.agregarEnrutador();
    }


    else if(opcion=="2"){
        string nombre;
        cout<<"Ingrese el nombre del enrutador:";
        cin>>nombre;
        routerA.eliminarEnrutador();
    }

    else if(opcion=="3"){

        routerA.cambiarCosto();

    }

    else{
        menuPrincipal();

    }

}

void menuPrincipal(){

    Routers routerA("A");
    string opcion;
    cout<<"**BIENVENIDO AL MENU PRINCIPAL**"<<endl;
    cout<<"1. Apartado de Routers."<<endl<< "2. Apartado de Red." << endl << "3. Tabla." << endl << "*Ingrese cualquier otro numero para salir del sistema.*" << endl << "Opcion: ";
    cin>>opcion;

    if(opcion=="1"){
        menuRouters();


    }
    else if(opcion=="2"){
        menuRed();

    }
    else if(opcion=="3"){
        routerA.mostrarTablaEnrutamiento();

    }
    else{

        menuPrincipal();
    }

}
