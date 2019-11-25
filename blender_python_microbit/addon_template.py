import bpy
import math
import serial


class MicroBitOperator(bpy.types.Operator):
    bl_idname = "kitteens.micro_bit_operator"
    bl_label = "MicroBit Operator"

    _timer = None    
    
    def do_stuff(self, context):
        # code goes here
    

    def modal(self, context, event):
        if event.type == 'ESC':
            self.cancel(context)
            return {'CANCELLED'}

        if event.type == 'TIMER':
            self.do_stuff(context)

        return {'PASS_THROUGH'}

    def execute(self, context):
        # code goes here
        self._timer = context.window_manager.event_timer_add(0.05, context.window) 
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        # code goes here
        context.window_manager.event_timer_remove(self._timer)
        return {'CANCELLED'}


def register():
    bpy.utils.register_class(MicroBitOperator)


def unregister():
    bpy.utils.unregister_class(MicroBitOperator)


if __name__ == "__main__":
    register()
