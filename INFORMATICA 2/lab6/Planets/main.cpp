#include <iostream>
#include <fstream>
#include "cuerpo.h"

#define N_PLANETS 5

int main(int argc, char *argv[])

{
    if(argc<2){
        cout << "Faltan argumentos.\n";
        return 0;
    }
    Cuerpo* planets = new Cuerpo[N_PLANETS];
    planets[0].set_body(0,20000,50000,700,0.5,0);
    planets[1].set_body(0,-20000,50000,700,-0.5,0);
    planets[2].set_body(-2000, 20000,25,300,0.5,-5);
    planets[3].set_body(0,-17000,100,300,-4,0);
    planets[4].set_body(0,-25000,200,300,3,0);

    ofstream fout;
    fout.open(argv[1]);
    for(int i=0; i<100000; i++){
        for(int i=0;i<N_PLANETS;i++){
            fout << planets[i].get_px()<<"- "<<planets[i].get_py()<<"\t";
        }
        fout<<endl;

        for(int i=0; i<N_PLANETS; i++){
            for(int j=0; j<N_PLANETS;j++){
                if(i!=j){
                    planets[i].add_acc(planets[j]);
                }
            }
        }

        for(int i=0;i<N_PLANETS;i++){
            planets[i].calc_pos(2);
        }
    }
    fout.close();
    return 0;
}
