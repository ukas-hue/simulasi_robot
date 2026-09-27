import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time


class MoverNode(Node):

    def __init__(self):
        super().__init__('mover_node')

        self.publisher_ = self.create_publisher(
            Twist,
            'cmd_vel',
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.timer_callback
        )

        self.start_time = time.time()


    def timer_callback(self):

        msg = Twist()

        t = time.time() - self.start_time


        # =========================
        # Parameter robot
        # =========================

        kecepatan_maju = 0.4
        kecepatan_putar = 0.5


        # Durasi gerakan
        maju_panjang = 5.0
        maju_pendek = 2.5

        # waktu rotasi 90 derajat
        putar_90 = 3.2


        # Total waktu tiap tahap

        tahap1 = maju_panjang

        tahap2 = tahap1 + putar_90

        tahap3 = tahap2 + maju_pendek

        tahap4 = tahap3 + putar_90

        tahap5 = tahap4 + maju_panjang

        tahap6 = tahap5 + putar_90

        tahap7 = tahap6 + maju_pendek

        tahap8 = tahap7 + putar_90



        # =========================
        # GERAK PERSEGI PANJANG
        # =========================


        if t < tahap1:

            # sisi panjang pertama
            msg.linear.x = kecepatan_maju
            msg.angular.z = 0.0

            self.get_logger().info(
                "Maju sisi panjang 1"
            )


        elif t < tahap2:

            # putar kiri 90
            msg.linear.x = 0.0
            msg.angular.z = kecepatan_putar

            self.get_logger().info(
                "Putar kiri 90 derajat"
            )


        elif t < tahap3:

            # sisi pendek pertama
            msg.linear.x = kecepatan_maju
            msg.angular.z = 0.0

            self.get_logger().info(
                "Maju sisi pendek 1"
            )


        elif t < tahap4:

            msg.linear.x = 0.0
            msg.angular.z = kecepatan_putar

            self.get_logger().info(
                "Putar kiri 90 derajat"
            )


        elif t < tahap5:

            # sisi panjang kedua
            msg.linear.x = kecepatan_maju
            msg.angular.z = 0.0

            self.get_logger().info(
                "Maju sisi panjang 2"
            )


        elif t < tahap6:

            msg.linear.x = 0.0
            msg.angular.z = kecepatan_putar

            self.get_logger().info(
                "Putar kiri 90 derajat"
            )


        elif t < tahap7:

            # sisi pendek kedua
            msg.linear.x = kecepatan_maju
            msg.angular.z = 0.0

            self.get_logger().info(
                "Maju sisi pendek 2"
            )


        elif t < tahap8:

            # kembali arah awal
            msg.linear.x = 0.0
            msg.angular.z = kecepatan_putar

            self.get_logger().info(
                "Putar terakhir"
            )


        else:

            msg.linear.x = 0.0
            msg.angular.z = 0.0

            self.get_logger().info(
                "Robot berhenti"
            )

            self.publisher_.publish(msg)

            self.timer.cancel()

            rclpy.shutdown()

            return



        self.publisher_.publish(msg)



def main(args=None):

    rclpy.init(args=args)

    node = MoverNode()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    finally:

        node.destroy_node()

        if rclpy.ok():
            rclpy.shutdown()



if __name__ == '__main__':
    main()