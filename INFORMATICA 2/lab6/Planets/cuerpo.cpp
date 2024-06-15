#include "cuerpo.h"

Cuerpo::Cuerpo(float px_, float py_, float mass_, float rad_, float vx_, float vy_):px(px_),py(py_),vx(vx_),vy(vy_),mass(mass_),rad(rad_)
{
    ax=ay=0;
}

void Cuerpo::set_body(float px_, float py_, float mass_, float rad_, float vx_, float vy_)
{
    px=px_;
    py=py_;
    vx=vx_;
    vy=vy_;
    mass=mass_;
    rad=rad_;
    ax=ay=0;
}

float Cuerpo::get_px(){
    return px;
}

float Cuerpo::get_py(){
    return py;
}
float Cuerpo::get_mass(){
    return mass;
}

void Cuerpo::add_acc(Cuerpo& c2){
    float acc, ang, d2;
    d2=(px-c2.get_px())*(px-c2.get_px())+(py-c2.get_py())*(py-c2.get_py());
    acc=c2.get_mass()/d2;
    ang=atan2(c2.get_py()-py,c2.get_px()-px);
    ax+=acc*cos(ang);
    ay+=acc*sin(ang);
}

void Cuerpo::calc_pos(float dt){
    px+=vx*dt+ax*dt*dt/2;
    py+=vy*dt+ay*dt*dt/2;
    vx+=ax*dt;
    vy+=ay*dt;
    ax=ay=0;

}
