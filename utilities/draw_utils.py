def center_on_surf(surf, rect):
    surf_centerx = surf.get_width() // 2
    surf_centery = surf.get_height() // 2

    rec_centerx = rect.width // 2
    rec_centery = rect.height // 2

    topleftx = surf_centerx - rec_centerx
    toplefty = surf_centery - rec_centery

    return((topleftx, toplefty, rect.width, rect.height))

