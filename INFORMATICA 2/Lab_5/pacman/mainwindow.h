#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QGraphicsScene>
#include <QGraphicsView>
#include <QTimer>
#include <QDebug>
#include <QKeyEvent>
#include <QGraphicsPixmapItem>
#include <QList>
#include <cstdlib>


QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT


public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();


private slots:
    void mover();
    void mover_fantasma();


    void on_lcdNumber_overflow();

private:
    QTimer *timer;
    QTimer * timer2;
    Ui::MainWindow *ui;
    QGraphicsScene *scene;
    QGraphicsPixmapItem *pacman;
    QGraphicsRectItem *rectangulo;
    QGraphicsRectItem *rectangulo2;
    int cont = 0;
    void keyPressEvent(QKeyEvent *e);
    void keyReleaseEvent(QKeyEvent *e);
    int cont2 = 0;
    //static int cont2;
    QList <QGraphicsRectItem*> rec;
    QGraphicsPixmapItem *fantasma;
    int reco = 0;
    QList<int> recorrido;
    int direc = 0;
    QList<int> direccion;
    bool col(QGraphicsPixmapItem* );
    QList<QGraphicsPixmapItem*> point;
    int point2 = 0;
    bool game = true;


};
#endif // MAINWINDOW_H
