#ifndef CUERPO_H
#define CUERPO_H

#include <iostream>
#include <cmath>
using namespace std;
class Cuerpo
{
private:
    float px;
    float py;
    float vx;
    float vy;
    float ax;
    float ay;
    float mass;
    float rad;

public:
    Cuerpo(float px_=0, float py_=0, float mass_=1, float rad_=1, float vx_=0, float vy_=0);
    void set_body(float px_, float py_, float mass_, float rad_, float vx_=0, float vy_=0);
    float get_px();
    float get_py();
    float get_mass();
    void add_acc(Cuerpo& c2);
    void calc_pos(float dt);
};

#endif // CUERPO_H
