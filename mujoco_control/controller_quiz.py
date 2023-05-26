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

    
    def control(self,theta:np.ndarray,x_target:np.ndarray,kp,kd,is_view=True):
        """
        今の角度と目的の手先位置から,PD制御で必要な角速度を出力する関数

        :param theta: 今の角度
        :param x_target: 目的の手先位置
        :param kp: Pゲイン
        :param kd: Dゲイン
        :return theta_vel: 必要な関節角速度
        """

        x_end=self.forward_kinematics(theta=np.array(theta)) #今の手先位置の計算
        x_vel=self.pd_control(x_target=np.array(x_target),x_end=np.array(x_end),kp=kp,kd=kd) #PD制御で必要な手先の速度を計算
        theta_vel=self.to_joint_velocity(x_vel=np.array(x_vel),theta=np.array(theta)) #ヤコビアンを使って手先の速度を関節角速度に変換

        if is_view: #描画用に関節位置の保存
            self._save_joint_for_view(theta=theta)

        return np.array(theta_vel)
    
    
    def forward_kinematics(self,theta:np.ndarray)->np.ndarray:
        """
        今の角度から手先の位置を計算する関数

        :param theta: 今の角度 [θ0,θ1,θ2] (根本の方0,手先の方2)
        :type theta: numpy.ndarray
        :return x_end: 手先の位置 [x,y]
        :type x_end:numpy.ndarray
        """

        ##ここに今の関節角から手先の位置'x_end'を求めるプログラムを書く
        ##'x_end'はリストで[手先のx座標,手先のy座標]を返すようにする

        x_end=np.array([0.6,0.6]) #←消してok
        
        ##

        return x_end

    def pd_control(self,x_target:np.ndarray,x_end:np.ndarray,kp:float,kd:float)->np.ndarray:
        """
        目的の位置と今の位置から必要な手先の速度をPD制御で計算する

        :param x_target: 目的の手先位置 [x,y]
        :param x_end: 今の手先位置 [x,y]
        :param kp: P制御のゲイン
        :param kd: D制御のゲイン
        :return x_vel: 必要な手先の速度 [v_x,v_y]
        """

        ##もう完成してるからいじらなくて大丈夫

        e=x_target-x_end #手先の誤差
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

        ##ここに「PD制御で計算した手先のxy速度」と「今の関節角度」から「関節角速度'theta_vel'」を求めるコードを書く
        ## 'theta_vel'はリストで[根本のジョイント角速度,真ん中のジョイント角速度,手先側のジョイント角速度]を返すようにする
        
        theta_vel=([0,0,0]) #←消してok
        
        ##

        return theta_vel
    

    def _save_joint_for_view(self,theta:np.ndarray):
        """
        描画用に関節角を保存しているだけ
        気にしなくていい
        """

        x_joint0=np.array([0,self.L0]) 
        x_joint1=x_joint0+self.L1*np.array([np.sin(theta[0]),np.cos(theta[0])])
        x_joint2=x_joint1+self.L2*np.array([np.sin(theta[0]+theta[1]),np.cos(theta[0]+theta[1])]) 
        x_end=x_joint2+self.L3*np.array([np.sin(theta[0]+theta[1]+theta[2]),np.cos(theta[0]+theta[1]+theta[2])])

        ##描画用に保存してるだけ
        self.joint_vec["joint0"]=x_joint0
        self.joint_vec["joint1"]=x_joint1
        self.joint_vec["joint2"]=x_joint2
        self.joint_vec["endeffector"]=x_end
        ##



def test():
    """
    上手くコントローラークラスができてるかのテストプログラム
    """

    ##アニメーション用
    import matplotlib.pyplot as plt
    from matplotlib.animation import ArtistAnimation
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.set_aspect("equal")
    frames=[]
    ##


    theta=np.array([np.pi/6,np.pi/6,np.pi/6]) #初期角度
    x_target=np.array([0.5,0.3]) #ターゲット位置
    dt=0.01 #微小時間

    controller=Controller(dt=dt) #アームのコントローラー

    loop_num=100
    for t in range(loop_num):

        theta_vel=controller.control(theta=theta,x_target=x_target,kp=3,kd=0.1) #必要な角速度の計算
        theta+=np.array(theta_vel)*dt #アームの角度の更新

        ##アニメーションしてるだけ
        joints=np.array(list(controller.joint_vec.values()))
        joint_x,joint_y=joints[:,0],joints[:,1]
        frame_target=ax.plot(x_target[0],x_target[1],"x",color="red")
        joint_x=np.concatenate([[0],joints[:,0].flatten()])
        joint_y=np.concatenate([[0],joints[:,1].flatten()])
        frame=ax.plot(joint_x,joint_y,marker="o",color="blue")
        frames.append(frame+frame_target)
        ##
        
    
    ani=ArtistAnimation(fig=fig,artists=frames,interval=100)
    plt.show()


if __name__=="__main__":
    test()