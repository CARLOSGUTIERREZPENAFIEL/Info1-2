#include "scenep.h"
#include "mainwindow.h"
#include <QGraphicsSceneMouseEvent>
#include <QDebug>
#include <QLCDNumber>

SceneP::SceneP(MainWindow *parent) : QGraphicsScene(0.0, 0.0, 710, 710, parent), mainWindow(parent)
{
    setBackgroundBrush(QBrush(Qt::darkBlue));

    mapa_pacman = new QGraphicsPixmapItem();
    addItem(mapa_pacman);
    mapa_pacman->setPixmap(QPixmap(":/spr/mapaPacman.png"));
    mapa_pacman->setScale(1);
    mapa_pacman->setPos(0,0);

    pacman = new QGraphicsPixmapItem();
    addItem(pacman);
    pacman->setPixmap(QPixmap(":/spr/pacman0.png"));
    pacman->setScale(0.63);
    pacman->setPos(340,516);

    for(int i=0;i<4;i++)
    {
        QGraphicsPixmapItem* Blinky = new QGraphicsPixmapItem();
        QPixmap BlinkyPixmap(":/spr/blinky.png");
        Blinky->setPixmap(BlinkyPixmap);
        Blinky->setScale(0.8);
        Blinky->setPos(336+(i*30), 240);
        addItem(Blinky);
        fantasmas.append(Blinky);
        fantasmasOriginales.append(BlinkyPixmap);
    }
    Mov = new QTimer(this);
    Mov->start(10);
    connect(Mov, SIGNAL(timeout()), this, SLOT(movimiento_pacman()));

    potenciadoTimer = new QTimer(this);
    potenciadoTimer->setSingleShot(true);
    connect(potenciadoTimer, SIGNAL(timeout()), this, SLOT(desactivarPotenciado()));

    // Añadiendo comida en diferentes posiciones
    for (int i = 0; i < 26; ++i) { //primerfilita
        int x = 34 + (i * 25);
        if (x > 330 && x < 379) {
            continue;
        }
        comida.append(addRect(x, 24, 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
    }
    for (int i = 0; i < 26; ++i) { //2filita
        int x = 34 + (i * 25);
        comida.append(addRect(x, 124, 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
    }
    for (int i = 0; i < 26; ++i) { //3filita
        int x = 34 + (i * 25);
        if ((x > 180 && x < 230) || (x>328 && x<377) || (x>480 && x<528)) {
            continue;
        }
        comida.append(addRect(x, 174, 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
    }
    for (int i = 0; i < 26; ++i) { //4filita
        int x = 34 + (i * 25);
        if (x > 330 && x < 379) {
            continue;
        }
        comida.append(addRect(x, 449, 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
    }
    for (int i = 1; i < 25; ++i) { //5filita
        int x = 34 + (i * 25);
        if ((x > 330 && x < 379) || (x > 100 && x < 150) || (x > 550 && x < 600)) {
            continue;
        }
        comida.append(addRect(x, 524, 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
    }
    for (int i = 0; i < 26; ++i) { //6filita
        int x = 34 + (i * 25);
        if ((x > 180 && x < 230) || (x>328 && x<377) || (x>480 && x<528)) {
            continue;
        }
        comida.append(addRect(x, 599, 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
    }
    for (int i = 0; i < 26; ++i) { //7filita
        int x = 34 + (i * 25);
        comida.append(addRect(x, 649, 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
    }

    for (int i=1; i < 25; i++) { //primercolumna
        int y = 24 + (i * 25);
        if((y>168 && y<468) || (y>517 && y<590) || i==4 || i==23 || i==2){
            continue;
        }
        comida.append(addRect(34, y, 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
    }

    for (int i=1; i < 23; i++) { //segundac
        if(i==24 || i==4 || i==6 || i==17 || i==20){
            continue;
        }
        comida.append(addRect(159, 24+(i*25), 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
    }

    for (int i=4; i < 23; i++) { //tercerac
        int y = 24 + (i * 25);
        if((y>150 && y<517) || i==4 || i==6){
            continue;
        }
        comida.append(addRect(234, y, 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
    }

    for (int i=1; i < 25; i++) {//cuartac
        int y = 24 + (i * 25);
        if((y>140 && y<168) || (y>190 && y<468) || (y>540 && y<590) || i==4 || i==6 || i==23){
            continue;
        }
        comida.append(addRect(309, y, 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
    }
    for (int i=1; i < 25; i++) {//quintac
        int y = 24 + (i * 25);
        if((y>140 && y<168) || (y>190 && y<468) || (y>540 && y<590) || i==4 || i==6 || i==23){
            continue;
        }
        comida.append(addRect(384, y, 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
    }

    for (int i=4; i < 23; i++) { //sextac
        int y = 24 + (i * 25);
        if((y>150 && y<517) || i==4 || i==6){
            continue;
        }
        comida.append(addRect(459, y, 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
    }

    for (int i=1; i < 23; i++) { //septimacolumna
        if(i==24 || i==4 || i==6 || i==17 || i==20){
            continue;
        }
        comida.append(addRect(534, 24+(i*25), 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
    }

    for (int i=1; i < 25; i++) { //octavacolumna
        int y = 24 + (i * 25);
        if((y>168 && y<468) || (y>519 && y<590) || i==4 || i==2){
            continue;
        }
        comida.append(addRect(659, y, 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
    }
    for (int i=0; i < 2; i++){
        for (int j=0; j < 2; j++){
            comida.append(addRect(84+(j*525), 549+(i*25), 15, 15, QPen(Qt::darkYellow), QBrush(Qt::yellow)));
            comida_potenciada.append(addEllipse(31.8+(j*625), 71.8+(i*450), 20, 20, QPen(Qt::yellow), QBrush(Qt::darkYellow)));

        }
    }
}

void SceneP::movimiento_pacman()
{
    for (int i = 0; i < fantasmas.size(); ++i) {
        if ((pacman->collidesWithItem(fantasmas[i])) && (potenciado==false)) {
            vida=0;
            break;
        }
        else if((pacman->collidesWithItem(fantasmas[i])) && (potenciado==true)) {
            puntos+=200;
            fantasmas[i]->setPixmap(QPixmap(":/spr/ojos.png"));
            fantasmas[i]->setPos(336+(30*i), 325);
            break;
        }
    }
    if (mainWindow) {
        QLCDNumber *punts = mainWindow->findChild<QLCDNumber*>("punts");
        if (punts) {
            punts->display(puntos);
        }
    }
    if(pacman->pos().x()<0){
        pacman->setPos(pacman->pos().x()+700,pacman->pos().y());
    }
    else if(pacman->pos().x()>700){
        pacman->setPos(pacman->pos().x()-700,pacman->pos().y());
    }
    if(direccion==1)
    {
        pacman->setPos(pacman->pos().x()-1,pacman->pos().y());
        if(cont_img==0){
            pacman->setPixmap(QPixmap(":/spr/pacmanIZQUIERDA1.png"));
            cont_img=1;
        }
        else{
            pacman->setPixmap(QPixmap(":/spr/pacman0.png"));
            cont_img=0;
        }
        if(pacman->collidesWithItem(mapa_pacman)){
            direccion=0;
            pacman->setPos(pacman->pos().x()+1,pacman->pos().y());
        }
    } else if(direccion==2)
    {
        pacman->setPos(pacman->pos().x()+1,pacman->pos().y());
        if(cont_img==0){
            pacman->setPixmap(QPixmap(":/spr/pacmanDERECHA1"));
            cont_img=1;
        }
        else{
            pacman->setPixmap(QPixmap(":/spr/pacman0.png"));
            cont_img=0;
        }
        if(pacman->collidesWithItem(mapa_pacman)){
            direccion=0;
            pacman->setPos(pacman->pos().x()-1,pacman->pos().y());
        }
    } else if(direccion==3)
    {
        pacman->setPos(pacman->pos().x(),pacman->pos().y()-1);
        if(cont_img==0){
            pacman->setPixmap(QPixmap(":/spr/pacmanARRIBA1"));
            cont_img=1;
        }
        else{
            pacman->setPixmap(QPixmap(":/spr/pacman0.png"));
            cont_img=0;
        }
        if(pacman->collidesWithItem(mapa_pacman)){
            direccion=0;
            pacman->setPos(pacman->pos().x(),pacman->pos().y()+1);
        }
    } else if(direccion==4)
    {
        pacman->setPos(pacman->pos().x(),pacman->pos().y()+1);
        if(cont_img==0){
            pacman->setPixmap(QPixmap(":/spr/pacmanABAJO1"));
            cont_img=1;
        }
        else{
            pacman->setPixmap(QPixmap(":/spr/pacman0.png"));
            cont_img=0;
        }
        if(pacman->collidesWithItem(mapa_pacman)){
            direccion=0;
            pacman->setPos(pacman->pos().x(),pacman->pos().y()-1);
        }
    }

    for (int i = 0; i < comida.size(); ++i) {
        if (pacman->collidesWithItem(comida[i])) {
            removeItem(comida[i]);
            delete comida[i];
            comida.removeAt(i);
            puntos+=10;
            break;
        }
    }
    for (int i = 0; i < comida_potenciada.size(); ++i) {
        if (pacman->collidesWithItem(comida_potenciada[i])) {
            removeItem(comida_potenciada[i]);
            delete comida_potenciada[i];
            comida_potenciada.removeAt(i);
            for(int j = 0; j < fantasmas.size(); j++){
                fantasmas[j]->setPixmap(QPixmap(":/spr/fantasmasBlue.png"));
            }
            potenciado = true;
            puntos+=50;
            potenciadoTimer->start(15000);
            break;
        }
    }

}

void SceneP::desactivarPotenciado()
{
    for(int j = 0; j < fantasmas.size(); j++){
        fantasmas[j]->setPixmap(fantasmasOriginales[j]);
    }
    potenciado = false;
}


void SceneP::keyPressEvent(QKeyEvent *e)
{
    if(vida==0){
        direccion=0;
        return;
    }
    if(e->key()==Qt::Key_A)
    {
        direccion=1;
    } else if(e->key()==Qt::Key_D)
    {
        direccion=2;
    } else if(e->key()==Qt::Key_W)
    {
        direccion=3;
    } else if(e->key()==Qt::Key_S)
    {
        direccion=4;
    }
}

void SceneP::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
{
    QPointF mousePosition = event->scenePos();
    qDebug() << "Mouse Position:" << mousePosition;
    emit mousePositionChanged(mousePosition);
}
