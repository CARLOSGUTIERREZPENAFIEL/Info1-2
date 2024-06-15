#include "mainwindow.h"

#include <QApplication>
#include <QGraphicsScene>
#include <QGraphicsView>
#include <QTimer>
#include <QGraphicsEllipseItem>
#include <cmath>
#include <QDebug>
#include <QPushButton>
#include <QVBoxLayout>
#include <QObject>

void updateValues(double &xIn, double &yIn, double &tiempoX, double &tiempoY, double &velX, double &velY, double &ang, int &dir, bool &colX, QGraphicsEllipseItem &particle);

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    //Definir la escena y mostrarla

    QGraphicsScene scene;
    QGraphicsView view(&scene);
    scene.setSceneRect(0,0,900,700);
    view.setFixedSize(1000, 800);
    view.show();

    //Crear la particula y dibujarla

    QGraphicsEllipseItem particle(-5, -5, 20, 20);
    particle.setBrush(Qt::darkBlue);
    scene.addItem(&particle);

    //Definir variables y constantes:
    double tiempoX, tiempoY = 0;
    bool colX = true;

    //aceleracion debido a la gravedad
    double g = 9.81;

    //Coordenadas en x,y
    double xIn = 50;
    double yIn = 250;
    double x = xIn;
    double y = yIn;

    //Velocidad y ángulo inicial
    double velIn = 40;
    double ang = 45;
    double velInX = velIn * cos(ang * (M_PI/180)); //ang* (M_PI/180)
    double velInY = velIn * sin(ang * (M_PI/180));
    double velX = velInX; //la vel en x siempre será la misma
    double velY = velInY;

    int dir=1;

    //Definir el timer y las rutinas al interior
    QTimer timer;
    //conectar la señal al timeout del temporizador a una funcion lambda
    QObject::connect(&timer, &QTimer::timeout, [&]()
        {
        x = xIn + velX * tiempoX * dir;
        y = yIn - (velInY * tiempoY - 0.5 * g * tiempoY * tiempoY);
        velY = velInY - g * tiempoY;

        //Si hay una colision, recalculamos parametros

        //Colisiones en el eje horizontal
        if(x > scene.width() - particle.boundingRect().width() || x < particle.boundingRect().width())
        {
            colX = true;
            //particle.setX(scene.width() - particle.boundingRect().width() - 2)
            updateValues(xIn, yIn, tiempoX, tiempoY, velX, velY, ang, dir, colX, particle);

            qDebug() << "Choque en X";
            //timer.stop;
        }

        //Colisiones en el eje vertical

        //Actualizar la posicion de la particula
        particle.setPos(x,y);

        //Actualizar tiempo
        tiempoX += 0.5;
        tiempoY += 0.5;
        qDebug() << velY << velX;

        if (y > scene.height() - particle.boundingRect().height())
        {
            yIn = scene.height() - particle.boundingRect().height() - 1;
            colX = false;
            updateValues(xIn, yIn, tiempoX, tiempoY, velX, velY, ang, dir, colX, particle);

            velIn = sqrt(pow(velX, 2) + pow(velY, 2)) * 0.5;
            qDebug() << "angle " << ang << " " << velY << velX << " " << x << y << velIn << yIn;

            //Condicion para parar el rebote
            if(qAbs(velY) < 1.0)
            {
                velY = 0;
                timer.stop();
            }

        }
    });

    QPushButton pushButton("Change Gravity");
    QObject::connect(&pushButton, &QPushButton::clicked, [&]()
    {
        g *= 2;
    });

    QVBoxLayout layaout;
    layaout.addWidget(&view);
    layaout.addWidget(&pushButton);

    QWidget mainWidget;
    mainWidget.setLayout(&layaout);
    mainWidget.show();

    timer.start(50);

    return a.exec();
}

void updateValues(double &xIn, double &yIn, double &tiempoX, double &tiempoY, double &velX, double &velY, double &ang, int &dir, bool &colX, QGraphicsEllipseItem &particle)
{
    if(colX)
    {
        dir=dir*(-1);
        xIn = particle.x();
        tiempoX = 0;
    }
    else
    {
        //yIn = scene.height()-particle.boundingRect().height()-1;
        xIn = particle.x();
        ang = -atan2(velY, velX) * 180 / M_PI;
        tiempoY = 0;
        tiempoX = 0;
        //velIn = sqrt(pow(velx, 2) + pow(velY * 0.8, 2));
    }
}
