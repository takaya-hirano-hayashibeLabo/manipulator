"""
ロボットアームを制御するプログラム

初めは実行しても,アームは動かない(描画はされる)

このコードの
'forward_kinematics'と
'to_jonit_velocity'を
編集してアームが動くようにプログラムを書こう
"""


import numpy as np
from copy import deepcopy


class Controller():

    def __init__(self,dt):
        """
        マニピュレータをコントロールするクラス

        :param dt: 微小時間
        """
        self.dt=dt

        #マニピュレータのパラメータ
        self.L0=0.2848
        self.L1=0.4208
        self.L2=0.3143
        self.L3=0.1674

        self.e_prev=np.zeros(2) #D制御のために,前回の誤差を覚えておく

        self.joint_vec={} #描画用のジョイントベクトル

    
    def control(self,theta:np.ndarray,x_target:np.ndarray,kp,kd):
        """
        今の角度と目的の手先位置から,PD制御で必要な角速度を出力する関数

        :param theta: 今の角度
        :param x_target: 目的の手先位置
        :param kp: Pゲイン
        :param kd: Dゲイン
        :return theta_vel: 必要な関節角速度
        """

        x_pos=self.forward_kinematics(theta=np.array(theta)) #今の手先位置の計算
        x_vel=self.pd_control(x_target=np.array(x_target),x_pos=x_pos,kp=kp,kd=kd) #PD制御で必要な手先の速度を計算
        theta_vel=self.to_joint_velocity(x_vel=x_vel,theta=np.array(theta)) #ヤコビアンを使って手先の速度を関節角速度に変換

        return theta_vel

    
    def forward_kinematics(self,theta:np.ndarray)->np.ndarray:
        """
        今の角度から手先の位置を計算する関数

        :param theta: 今の角度 [θ0,θ1,θ2] (根本の方0,手先の方2)
        :type theta: numpy.ndarray
        :return x_end: 手先の位置 [x,y]
        :type x_pos:numpy.ndarray
        """

        ##ここに順運動学の式を書く
        x_joint0=np.array([0,0.2848])#joint0(土台の先端)の位置ベクトル
        x_joint1=np.array([0.2104,0.6492])#joint1の位置ベクトル
        x_joint2=np.array([0.4825,0.8063])#joint2の位置ベクトル
        x_pos=np.array([0.65,0.806])#手先の位置ベクトル
        ##

        ##描画用に保存してるだけ
        self.joint_vec["joint0"]=x_joint0
        self.joint_vec["joint1"]=x_joint1
        self.joint_vec["joint2"]=x_joint2
        self.joint_vec["endeffector"]=x_pos
        ##

        return x_pos

    def pd_control(self,x_target:np.ndarray,x_pos:np.ndarray,kp:float,kd:float)->np.ndarray:
        """
        目的の位置と今の位置から必要な手先の速度を計算する

        :param x_target: 目的の手先位置 [x,y]
        :param x_pos: 今の手先位置 [x,y]
        :param kp: P制御のゲイン
        :param kd: D制御のゲイン
        :return x_vel: 必要な手先の速度 [v_x,v_y]
        """

        e=x_target-x_pos #手先の誤差
        e_vel=(e-self.e_prev)/self.dt #手先誤差の速度
        self.e_prev=deepcopy(e) #手先誤差の記憶

        x_vel=kp*e+kd*e_vel

        return x_vel

    def to_joint_velocity(self,x_vel:np.ndarray,theta:np.ndarray)->np.ndarray:
        """
        必要な手先の速度と今の関節角度から, ヤコビアンを用いて, 必要な関節角速度を計算する
        
        :param x_vel: 必要な手先の速度 [v_x,v_y]
        :param theta: 今の関節角度 [θ0,θ1,θ2](根本の方θ0,手先の方θ2)
        :retrun theta_vel: 必要な関節角速度 [v_θ0,v_θ1,v_θ2]
        """

        ##手先の速度と今の角度から関節角速度を求める式を書く
        ##返り値は1次元リスト[v_θ0,v_θ1,v_θ2] (θ0が根本の方,θ2が手先の方)

        return np.array([0,0,0])


def test():
    """
    ***ここはいじらなくてもいい***

    上手くコントローラークラスができてるかのテストプログラム

    上手くいってるときは, ターゲット(赤のバツ印)に手先が近づく
    """

    import matplotlib.pyplot as plt
    from matplotlib.animation import ArtistAnimation


    theta=np.array([np.pi/6,np.pi/6,np.pi/6]) #初期角度
    x_target=np.array([0.5,0.8]) #ターゲット位置
    dt=0.05 #微小時間
    loop_num=100

    controller=Controller(dt=dt) #コントローラーの準備

    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    frames=[]

    for t in range(loop_num):

        theta_vel=controller.control(theta=theta,x_target=x_target,kp=1,kd=0.5) #必要な角速度の計算

        ##描画してるだけ
        joints=np.array(list(controller.joint_vec.values()))
        frame_target=ax.plot(x_target[0],x_target[1],"x",color="red")
        frame=ax.plot(joints[:,0],joints[:,1],marker="o",color="blue")
        frames.append(frame+frame_target)
        ##

        theta+=theta_vel*dt #角度の制御
    
    ani=ArtistAnimation(fig=fig,artists=frames,interval=100)
    plt.show()


if __name__=="__main__":
    test()