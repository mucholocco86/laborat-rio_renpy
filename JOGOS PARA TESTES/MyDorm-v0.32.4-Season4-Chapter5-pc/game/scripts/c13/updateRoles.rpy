label updateRoles:
    python:
        if dap._var ("route"):
            dap.roles.addRole (_("amante"))

        if eil._var ("route"):
            eil.roles.delete (_("amiga con beneficios"))
            eil.roles.addRole (_("amante"))

        if emm._var ("route"):
            emm.roles.addRole (_("amante"))

        if eri._var ("route"):
            eri.roles.addRole (_("amante"))

        if mad._var ("route"):
            mad.roles.delete (_("conocida"))
            mad.roles.addRole (_("amante"))

        if mar._var ("route"):
            mar.roles.addRole (_("amante"))

        if nor._var ("route"):
            nor.roles.addRole (_("amante"))

        if oma._var ("route"):
            oma.roles.delete (_("conocida"))
            oma.roles.addRole (_("amante"))

        if sam._var ("route"):
            sam.roles.addRole (_("amante"))

        if sim._var ("route"):
            sim.roles.addRole (_("amante"))

        if sca._var ("route"):
            sca.roles.delete (_("conocida"))
            sca.roles.addRole (_("amante"))
    return