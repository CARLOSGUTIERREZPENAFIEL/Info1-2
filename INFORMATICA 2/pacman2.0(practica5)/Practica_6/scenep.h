#ifndef SCENEP_H
#define SCENEP_H

#include <QGraphicsScene>
#include <QGraphicsPixmapItem>
#include <qevent.h>
#include <QTimer>

class MainWindow;

class SceneP : public QGraphicsScene
{
    Q_OBJECT
public:
    SceneP(MainWindow *parent = nullptr);
protected:
    void keyPressEvent(QKeyEvent *e) override;
    void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override;
signals:
    void mousePositionChanged(const QPointF &position);
private slots:
    void movimiento_pacman();
    void desactivarPotenciado();
private:
    MainWindow *mainWindow;
    QGraphicsPixmapItem *mapa_pacman;
    QGraphicsPixmapItem *pacman;
    QTimer *Mov;
    QTimer *potenciadoTimer;

    QList<QGraphicsRectItem*> comida;
    QList<QGraphicsEllipseItem*> comida_potenciada;
    QList<QGraphicsPixmapItem*> fantasmas;
    QList<QPixmap> fantasmasOriginales;

    int direccion;
    int cont_img=0;
    int vida=1;
    int puntos=0;

    bool potenciado=false;
};

#endif // SCENEP_H
