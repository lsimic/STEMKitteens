import bpy
import math
import serial


# change this so it fits your port
ser = serial.Serial('COM3')


class MicroBitOperator(bpy.types.Operator):
	# you can choose a different name here
    bl_idname = "kitteens.micro_bit_operator"
    bl_label = "MicroBit Operator"

    _timer = None    
    
    def do_stuff(self, context):
        # code goes here
        msg = ser.readline()
        msg_parts = msg.decode('utf-8').strip('\n').split(',')
        rot_x = math.radians(int(msg_parts[0])*90/1000)
        rot_y = math.radians(int(msg_parts[1])*90/1000)
        rot_z = 0
		# You should use the name you used for the object. It is cube by default
        ob = context.scene.objects["Cube"]
        ob.rotation_euler = (rot_x, rot_y, rot_z)
    

    def modal(self, context, event):
        if event.type == 'ESC':
            self.cancel(context)
            return {'CANCELLED'}

        if event.type == 'TIMER':
            self.do_stuff(context)

        return {'PASS_THROUGH'}

    def execute(self, context):
        if not ser.is_open:
            ser.open()
        self._timer = context.window_manager.event_timer_add(0.05, context.window) 
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        if ser.is_open:
            ser.close()
        context.window_manager.event_timer_remove(self._timer)
        return {'CANCELLED'}


def register():
    bpy.utils.register_class(MicroBitOperator)


def unregister():
    bpy.utils.unregister_class(MicroBitOperator)


if __name__ == "__main__":
    register()
