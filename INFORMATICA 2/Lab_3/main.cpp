#include "metodos.h"

int main(){
    int cant_bloques_usu;
    int doc_exist=0;
    int tipo_usuario, tipo_metodo, semilla;
    string clave_admin;
    char ban2;
    string nombreArchivo = "archivo.txt";
    int cant_us = cantidad_usuarios(nombreArchivo);
    string** us_totales = usuarios_totales(nombreArchivo);
    // Imprimir los datos (puedes modificar esto según tus necesidades)

    bool ban;
    do{
        cout << "Ingrese la opcion deseada: " << endl << endl << "1.Usuario administrador." << endl << "2.Usuario Cliente." << endl << "Opcion: ";
        cin >> tipo_usuario;
    } while((tipo_usuario<1) || (tipo_usuario>2));

    if(tipo_usuario==1){
        string clave = leerArchivo(nombreArchivo, 1);
        string* clave_codificada;
        string* bloques;
        do{
        cout << "Ingrese la clave, el metodo de codificacion usado, y su semilla." << endl << endl << "Clave: ";
        cin >> clave_admin;
        string binario_clave = convertir_a_binario(clave_admin);
        int tamanio = binario_clave.length();
        do{
            cout << "Metodo: ";
            cin >> tipo_metodo;
        } while((tipo_metodo<1) || (tipo_metodo>2));
        do{
            cout << "Ingrese una semilla: ";
            cin >> semilla;
        } while(semilla>=tamanio || semilla<1 );
        bloques= separar_en_bloques(binario_clave, semilla);
        int cant_bloques = stoi(bloques[0]);
        if(tipo_metodo==1){
            clave_codificada= metodo_1(bloques);
        }
        else{
            clave_codificada= metodo_2(bloques);
        }
        ban = comprobarClave(clave, clave_codificada, cant_bloques);
        if(ban==false){
            cout << endl << "La clave, el metodo, o la semilla no son validas, por favor intente de nuevo." << endl;
        }
        }while(ban==false);
        while(true){
            cout << endl <<"Desea ingresar un usuario? y/n: ";
            cin >> ban2;
            if(ban2=='y' || ban2=='Y'){
                string documento_usuario, clave_usuario, saldo_usuario;
                cout << "Ingrese el documento del usuario: ";
                cin >> documento_usuario;
                cout << "Ingrese la clave del usuario: ";
                cin >> clave_usuario;
                cout << "Ingrese el saldo del usuario: ";
                cin >> saldo_usuario;
                string documento_codificado = convertir_a_binario(documento_usuario);
                string clave_usuario_codificada = convertir_a_binario(clave_usuario);
                string saldo_usuario_codificado = convertir_a_binario(saldo_usuario);
                string* documento_codificado_separado = separar_en_bloques(documento_codificado, semilla);
                string* clave_codificada_separado = separar_en_bloques(clave_usuario_codificada, semilla);
                string* saldo_codificado_separado = separar_en_bloques(saldo_usuario_codificado, semilla);

                string* documento_codificado_m1 = metodo_1(documento_codificado_separado);
                string* clave_codificado_m1 = metodo_1(clave_codificada_separado);
                string* saldo_codificado_m1 = metodo_1(saldo_codificado_separado);

                int bloques_doc = stoi(documento_codificado_separado[0]);
                int bloques_cl = stoi(clave_codificada_separado[0]);
                int bloques_saldo = stoi(saldo_codificado_separado[0]);

                for(int i=0;i<cant_us;i=i+1){
                    string doc_archivo = us_totales[i][0];
                    bool comp_doc = comprobarClave(doc_archivo, documento_codificado_m1, bloques_doc);
                    if(comp_doc==true){
                        doc_exist = 1;
                    }

                }
                if(doc_exist==0){
                    string documento_codificado_m1_unido, clave_codificado_m1_unido, saldo_codificado_m1_unido;
                    for(int i=0;i<bloques_doc;i++){
                        documento_codificado_m1_unido+=documento_codificado_m1[i];
                    }
                    for(int i=0;i<bloques_cl;i++){
                        clave_codificado_m1_unido+=clave_codificado_m1[i];
                    }
                    for(int i=0;i<bloques_saldo;i++){
                        saldo_codificado_m1_unido+=saldo_codificado_m1[i];
                    }
                    aumentarTamano(us_totales, cant_us);
                    us_totales[cant_us-1][0]=documento_codificado_m1_unido;
                    us_totales[cant_us-1][1]=clave_codificado_m1_unido;
                    us_totales[cant_us-1][2]=saldo_codificado_m1_unido;
                    eliminar_datos();
                    actualizar_datos(us_totales, cant_us);


                }
                else{
                    cout << "El documento ya ha sido registrado anteriormente, por favor intente uno nuevo." << endl;
                    doc_exist=0;
                }

            }   
            else if(ban2=='n' || ban2=='N'){
                return 0;
            }
        }
        delete [] clave_codificada;
        delete [] bloques;
        for (int i = 0; i < cant_us; ++i) {
            delete [] us_totales[i];
        }
        delete [] us_totales;

    }
    else if(tipo_usuario==2){
        int usuario_temp;
        string documento_usuario, clave_usuario;
        cout << endl << "Ingrese el documento: ";
        cin >> documento_usuario;
        for(int i=0;i<cant_us;i=i+1){
            string doc_archivo = us_totales[i][0];
            string binario_doc = convertir_a_binario(documento_usuario);
            string* bloques_doc= separar_en_bloques(binario_doc,4);
            string* metodo1_doc= metodo_1(bloques_doc);
            string bloques_doc_num=bloques_doc[0];
            int cant_bloques_doc = stoi(bloques_doc_num);
            bool comp_doc_us = comprobarClave(doc_archivo, metodo1_doc, cant_bloques_doc);
            if(comp_doc_us==true){
                doc_exist = 1;
                usuario_temp=i;
            }
            delete [] bloques_doc;
            delete [] metodo1_doc;
        }
        if(doc_exist==1){
            int ban_clave=0;
            string usu_archivo=us_totales[usuario_temp][1];
            do{
            cout << "Ingrese la clave: ";
            cin >> clave_usuario;
            string binario_usu = convertir_a_binario(clave_usuario);
            string* bloques_usu= separar_en_bloques(binario_usu,4);
            string* metodo1_usu= metodo_1(bloques_usu);
            string cant_bloq_us=bloques_usu[0];
            cant_bloques_usu = stoi(cant_bloq_us);
            bool comp_clav_us = comprobarClave(usu_archivo, metodo1_usu, cant_bloques_usu);
            if(comp_clav_us==true){
                ban_clave = 1;
            }
            else{
                cout << "Clave incorrecta, intente de nuevo." << endl << endl;
            }
            }while(ban_clave==0);


            string opcion;
            cout<< "Seleccionar una opcion: "<<endl<<"1. Consultar saldo"<<endl<<"2. Retirar dinero"<<endl;
            cin>>opcion;
            if(opcion == "1"){
                string saldo1 = us_totales[usuario_temp][2];

                string* bloques = separar_en_bloques(saldo1, 4);
                string* bloques_bien = cambio_separar_bloques(bloques, stoi(bloques[0]));
                string* deco = decodificacion_metodo_1(bloques_bien,stoi(bloques[0]));

                string convertido = convertir_a_texto(deco,stoi(bloques[0]));

                cout<<"Tu saldo es de: "<<convertido<<" - 1000 pesos por la consulta"<<endl;
                int nuevo_saldo = stoi(convertido) - 1000;
                delete [] bloques;
                delete [] deco;
                delete [] bloques_bien;
                string binario = convertir_a_binario(to_string(nuevo_saldo));
                bloques = separar_en_bloques(binario, 4);
                string* metodo1 = metodo_1(bloques);
                string aux;
                for(int i = 0; i < to_string(nuevo_saldo).length()* 2; i++ ){
                    aux += metodo1[i];
                }
                us_totales[usuario_temp][2] = aux;
                eliminar_datos();
                actualizar_datos(us_totales, cant_us);
                delete[] metodo1;



            }
            else{
                string saldo1 = us_totales[usuario_temp][2];
                string* bloques = separar_en_bloques(saldo1, 4);
                string* bloques_bien = cambio_separar_bloques(bloques, stoi(bloques[0]));
                string* deco = decodificacion_metodo_1(bloques_bien,stoi(bloques[0]));
                string convertido = convertir_a_texto(deco,stoi(bloques[0]));

                cout<<"Tu saldo es de: "<<convertido <<endl;
                int retirar;
                cout<<"Ingrese el valor a retirar "<<endl;
                cin >> retirar;
                while (true) {
                    if(retirar >stoi(convertido) || stoi(convertido) - retirar < 1000){
                        cout<<"Saldo insuficiente, ingrese uno nuevo"<<endl;
                        cin>> retirar;
                    }
                    else{
                        break;
                    }
                }
                int nuevo_saldo = stoi(convertido)- retirar- 1000;
                delete [] bloques;
                delete [] deco;
                delete [] bloques_bien;
                string binario = convertir_a_binario(to_string(nuevo_saldo));
                bloques = separar_en_bloques(binario, 4);
                string* metodo1 = metodo_1(bloques);
                string aux;
                for(int i = 0; i < to_string(nuevo_saldo).length()* 2; i++ ){
                    aux += metodo1[i];
                }

                us_totales[usuario_temp][2] = aux;
                eliminar_datos();
                actualizar_datos(us_totales, cant_us);

            }




        }
        else{
            cout << "El documento no esta registrado.";
        }
    }


    return 0;

}
