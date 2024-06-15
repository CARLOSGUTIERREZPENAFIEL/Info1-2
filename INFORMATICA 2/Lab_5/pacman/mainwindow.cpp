
#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    scene = new QGraphicsScene();
    ui -> graphicsView -> setScene(scene);
    QImage fondo(":/fondo.png");
    ui -> graphicsView -> setBackgroundBrush(fondo);
    scene -> setSceneRect(1250,1050,1366,768);
    ui->graphicsView->scale(0.35,0.26);

    QPixmap pixMap(":/pacman0.png");
    pacman = new QGraphicsPixmapItem();
    scene -> addItem(pacman);
    pacman -> setPixmap(pixMap);
    pacman -> setScale(1.5);
    pacman -> setPos (1850,1465);

    timer = new QTimer(this);
    timer-> start(180);
    connect(timer,SIGNAL(timeout()),this,SLOT(mover()));

    QPen pen(Qt::blue, 3, Qt::SolidLine, Qt::RoundCap, Qt::RoundJoin);
    QBrush brush(Qt::blue);
    rec.append(scene->addRect(400, 260, 400, 140, pen, brush));
    rec.append(scene->addRect(1078, 260, 510, 140, pen, brush));
    rec.append(scene->addRect(2275, 260, 510, 140, pen, brush));
    rec.append(scene->addRect(3060, 260, 400, 140, pen, brush));
    rec.append(scene->addRect(400, 574, 400, 63, pen, brush));
    rec.append(scene->addRect(1480, 574, 900, 63, pen, brush));
    rec.append(scene->addRect(3060, 574, 400, 63, pen, brush));
    rec.append(scene->addRect(1870, 630, 120, 280, pen, brush));
    rec.append(scene->addRect(1075, 600, 140, 520, pen, brush));
    rec.append(scene->addRect(1200, 810, 400, 70, pen, brush));
    rec.append(scene->addRect(2650, 600, 140, 520, pen, brush));
    rec.append(scene->addRect(2280, 810, 400, 70, pen, brush));
    rec.append(scene->addRect(1445, 1370, 950, 20, pen, brush));
    rec.append(scene->addRect(1450, 1060, 20, 330, pen, brush));
    rec.append(scene->addRect(2370, 1060, 20, 330, pen, brush));
    rec.append(scene->addRect(1450, 1060, 320, 20, pen, brush));
    rec.append(scene->addRect(2070, 1060, 320, 20, pen, brush));
    rec.append(scene->addRect(1070, 1300, 140, 290, pen, brush));
    rec.append(scene->addRect(2650, 1300, 140, 290, pen, brush));
    rec.append(scene->addRect(1480, 1560, 900, 63, pen, brush));
    rec.append(scene->addRect(1870, 1600, 120, 280, pen, brush));
    rec.append(scene->addRect(1480, 2040, 900, 63, pen, brush));
    rec.append(scene->addRect(1870, 2070, 120, 280, pen, brush));
    rec.append(scene->addRect(1078, 1790, 510, 89, pen, brush));
    rec.append(scene->addRect(2275, 1790, 510, 89, pen, brush));
    rec.append(scene->addRect(400, 1790, 410, 89, pen, brush));
    rec.append(scene->addRect(3060, 1790, 410, 89, pen, brush));
    rec.append(scene->addRect(660, 1790, 140, 290, pen, brush));
    rec.append(scene->addRect(3060, 1790, 140, 290, pen, brush));
    rec.append(scene->addRect(400,2250 , 1200, 89, pen, brush));
    rec.append(scene->addRect(2280,2250 , 1200, 89, pen, brush));
    rec.append(scene->addRect(1070, 2040, 140, 290, pen, brush));
    rec.append(scene->addRect(2650, 2040, 140, 290, pen, brush));
    rec.append(scene->addRect(1870, 120, 120, 280, pen, brush));
    rec.append(scene->addRect(80, -10, 3650, 100, pen, brush));
    rec.append(scene->addRect(80, -10, 100, 3000, pen, brush));
    rec.append(scene->addRect(3700, -10, 100, 3000, pen, brush));
    rec.append(scene->addRect(80, 2500, 3650, 100, pen, brush));
    rec.append(scene->addRect(100, 2020, 250, 60, pen, brush));
    rec.append(scene->addRect(3500, 2020, 250, 60, pen, brush));
    rec.append(scene->addRect(80, 810, 700, 300, pen, brush));
    rec.append(scene->addRect(3060, 810, 700, 300, pen, brush));
    rec.append(scene->addRect(80, 1300, 700, 300, pen, brush));
    rec.append(scene->addRect(3060, 1300, 700, 300, pen, brush));
    rectangulo = scene->addRect(200, 1150, 100, 100);
    rectangulo2= scene-> addRect(3600, 1150, 100, 100);


    QPixmap f1(":/F1.png");
    fantasma = new QGraphicsPixmapItem();
    scene -> addItem(fantasma);
    fantasma -> setPixmap(f1);
    fantasma -> setScale(1.5);
    fantasma -> setPos (1870,1240);
    QPixmap punt(":/punto.png");



    timer2 = new QTimer(this);
    timer2-> start(180);
    connect(timer2,SIGNAL(timeout()),this,SLOT(mover_fantasma()));


    struct puntos {
        int x, y;
    };

    QVector<puntos> p = {

        {230, 100}, {430, 100}, {630, 100}, {830, 100}, {1030, 100}, {1230, 100}, {1430, 100}, {1630, 100}, {1830, 100}, {2030, 100}, {2230, 100}, {2430, 100},{2630,100},{2830,100},{3030,100},{3230,100},{3500,100},
        {230, 250}, {830, 250},  {1630, 250},  {2030, 250},{2830,250},{3500,250},
        {230, 400}, {430, 400}, {630, 400}, {830, 400}, {1030, 400}, {1230, 400}, {1430, 400}, {1630, 400}, {1830, 400}, {2030, 400}, {2230, 400}, {2430, 400},{2630,400},{2830,400},{3030,400},{3230,400},{3500,400},
        {230, 550},  {830, 550}, {1230, 550}, {2430, 550},{2830,550},{3500,550},
        {230, 650}, {430, 650}, {630, 650}, {830, 650}, {1230, 650}, {1430, 650}, {1630, 650}, {2030, 650}, {2230, 650}, {2430, 650},{2830,650},{3030,650},{3230,650},{3500,650},
        {830, 900},  {1230, 900}, {1430, 900}, {1630, 900}, {1830, 900}, {2030, 900}, {2230, 900}, {2430, 900},{2830,900},
        {230, 1130}, {430, 1130}, {630, 1130}, {830, 1130}, {1030, 1130}, {1230, 1130}, {2430, 1130},{2630,1130},{2830,1130},{3030,1130},{3230,1130},{3500,1130},
        {830, 1400}, {1230, 1400}, {1430, 1400}, {1630, 1400}, {1830, 1400}, {2030, 1400}, {2230, 1400}, {2430, 1400},{2830,1400},
        {230, 1630}, {430, 1630}, {630, 1630}, {830, 1630}, {1030, 1630}, {1230, 1630}, {1430, 1630}, {1630, 1630},  {2030, 1630}, {2230, 1630}, {2430, 1630},{2630,1630},{2830,1630},{3030,1630},{3230,1630},{3500,1630},
        {230, 1900}, {430,1900}, {830, 1900}, {1030, 1900}, {1230, 1900}, {1430, 1900}, {1630, 1900}, {1830, 1900}, {2030, 1900}, {2230, 1900}, {2430, 1900},{2630,1900},{2830,1900},{3230,1900},{3500,1900},
        {230, 2100}, {430, 2100}, {630, 2100}, {830, 2100}, {1230, 2100}, {1430, 2100}, {1630, 2100},  {2030, 2100}, {2230, 2100}, {2430, 2100},{2830,2100},{3030,2100},{3230,2100},{3500,2100},
        {230, 2350}, {430, 2350}, {630, 2350}, {830, 2350}, {1030, 2350}, {1230, 2350}, {1430, 2350}, {1630, 2350}, {1830, 2350}, {2030, 2350}, {2230, 2350}, {2430, 2350},{2630,2350},{2830,2350},{3030,2350},{3230,2350},{3500,2350},

        };


    for (const auto& p2 : p) {
        QGraphicsPixmapItem* pixmapItem = new QGraphicsPixmapItem(punt);
        pixmapItem -> setScale(7);
        pixmapItem->setPos(p2.x, p2.y);

        scene->addItem(pixmapItem);
        point.append(pixmapItem);
    }
}


bool MainWindow :: col(QGraphicsPixmapItem *cosa){
    for(int i = 0; i<point.length();i++){
        if(pacman->collidesWithItem(point[i])){
            scene -> removeItem(point[i]);
            point.removeAt(i);
            point2 ++;
            if(point2 == 30){
                timer2->stop();
                ui-> label-> setText("YOU WIN");
                game = false;
                qDebug()<<point2;
            }
            break;
        }
    }
    for (QGraphicsRectItem *rect : rec) {

        if (cosa->collidesWithItem(rect)) {

            //pacman->setPos(pacman->pos().x()-30,pacman->pos().y());

            return true;
        }
    }
    if(pacman-> collidesWithItem(fantasma)){
        game = false;
        ui->label-> setText("GAME OVER");
    }
    return false;

}
void MainWindow :: mover_fantasma(){

    int move = rand()%4+1;
    if(move == 1){
        fantasma-> moveBy(15,0);
        if(col(fantasma)){
        fantasma-> moveBy(-30,0);
        }
    }
    else if(move == 2){
        fantasma-> moveBy(-15,0);
        if(col(fantasma)){
            fantasma-> moveBy(+30,0);
        }

    }
    else if(move == 3){
        fantasma-> moveBy(0,15);
        if(col(fantasma)){
            fantasma-> moveBy(0,-30);
        }
    }
    else if(move == 4){
        fantasma-> moveBy(0,-15);
        if(col(fantasma)){
            fantasma-> moveBy(0,+30
                             );
        }
    }


}

void MainWindow :: mover(){
    cont += 1;
    if(cont >3){
        cont = 1;
    }

}


void MainWindow :: keyPressEvent(QKeyEvent *e){
    //timer -> start();
    //QPointF subjectPos = pacman ->pos();
    QPixmap pacman0(":/pacman0.png");
    QPixmap pacmanABAJO1(":/pacmanABAJO1.png");
    QPixmap pacmanABAJO2(":/pacmanABAJO2.png");
    QPixmap pacmanARRIBA1(":/pacmanARRIBA1.png");
    QPixmap pacmanARRIBA2(":/pacmanARRIBA2.png");
    QPixmap pacmanDERECHA1(":/pacmanDERECHA1.png");
    QPixmap pacmanDERECHA2(":/pacmanDERECHA2.png");
    QPixmap pacmanIZQUIERDA1(":/pacmanIZQUIERDA1.png");
    QPixmap pacmanIZQUIERDA2(":/pacmanIZQUIERDA2.png");
    if(game){

    if(e-> key() == Qt:: Key_D){
        if (cont == 1) {
            pacman->setPixmap(pacmanDERECHA1);

            //cont2 = 2;
        } else if (cont == 2) {
            pacman->setPixmap(pacmanDERECHA2);

            //cont2 == 3;
        } else if (cont == 3) {
            pacman->setPixmap(pacman0);

            //cont2 = 1;
        }

        if (pacman-> collidesWithItem(rectangulo2)){
            pacman-> setPos(300,1150);
        }


        pacman->setPos(pacman->pos().x()+15,pacman->pos().y());
        if(col(pacman) == true){
            pacman->setPos(pacman->pos().x()-30,pacman->pos().y());

        }





    }
    else if(e-> key() == Qt:: Key_W){
        if (cont == 1) {
            pacman->setPixmap(pacmanARRIBA1);

            //cont2 = 2;
        } else if (cont == 2) {
            pacman->setPixmap(pacmanARRIBA2);

            //cont2 == 3;
        } else if (cont == 3) {
            pacman->setPixmap(pacman0);

            //cont2 = 1;
        }
        // Mueve el pacman después de establecer el pixmap


        pacman->setPos(pacman->pos().x() , pacman->pos().y()-15);
        if(col(pacman) == true){
            pacman->setPos(pacman->pos().x(),pacman->pos().y()+30);

        }



    }
    else if(e-> key() == Qt:: Key_A){
        if(cont == 1){
            pacman -> setPixmap(pacmanIZQUIERDA1);


        }
        else if(cont == 2){
            pacman -> setPixmap(pacmanIZQUIERDA2);

        }
        else if(cont == 3){
            pacman -> setPixmap(pacman0);

        }
        if (pacman-> collidesWithItem(rectangulo)){
            pacman-> setPos(3500,1150);
        }

        pacman->setPos(pacman->pos().x() - 15, pacman->pos().y());

        if(col(pacman) == true){
            pacman->setPos(pacman->pos().x()+30,pacman->pos().y());

        }


    }
    else if(e-> key() == Qt:: Key_S){
        if(cont == 1){
            pacman -> setPixmap(pacmanABAJO1);


        }
        else if(cont == 2){
            pacman -> setPixmap(pacmanABAJO2);

        }
        else if(cont == 3){
            pacman -> setPixmap(pacman0);

        }

        pacman->setPos(pacman->pos().x() , pacman->pos().y()+15);
        if(col(pacman) == true){
            pacman->setPos(pacman->pos().x(),pacman->pos().y()-30);

        }


    }
    }
}
void MainWindow :: keyReleaseEvent(QKeyEvent *event){

}
MainWindow::~MainWindow()
{
    delete ui;
}


