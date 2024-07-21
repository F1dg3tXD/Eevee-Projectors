bl_info = {
    "name": "Eevee Projectors",
    "blender": (3, 0, 0),
    "category": "Object",
    "version": (1, 1, 0),
    "location": "View3D > Add > Light",
    "description": "Adds a new Projector light for Eevee that can project images or movies",
    "wiki_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
}

def register():
    from . import main
    main.register()

def unregister():
    from . import main
    main.unregister()

if __name__ == "__main__":
    register()
