# The NetIDE Network Engine
The **Network Engine** provides to unmodified SDN applications (called Modules in the Figure below) the runtime they expect. Additionally it implements a composition
mechanism to create new applications from previously implemented modules and to make them cooperating with modules running on top of the operator’s controller (represented by the
Server Controller in the Figure), effectively building a single Network Application.

The Network Engine follows the layered SDN controller approach proposed by the Open Networking Foundation. It comprises a client controller layer that executes the modules network applications are composed of and a server SDN controller layer that drives the underlying infrastructure.

The challenge is to integrate client and server controllers.
To maximize reuse, we use separate adaptors for the Southbound Interface (SBI), called Backend, and for the Northbound Interface (NBI), called Shim. This separation imposes a protocol between them, the NetIDE Intermediate
Protocol (see the full protocol specification in libraries/netip/docs).
In our first implementations [1] we have proved that the Shim/Backend structure connected by an intermediate protocol is feasible and sensible. However, they still left the fundamental component in these modules: the composition logic. This implied that it needed to be reimplemented for each controller framework we wanted to support. To overcome
this shortcoming, we introduce an intermediate layer, the Core: it hosts all logic and data structures that are independent of the particular controller frameworks and
communicates with both Shim and Backend using the same NetIDE Intermediate Protocol. The Core makes both Shim and Backend light-weight and easier to implement for new controllers.

This repository contains source code and documentation of the Core, Shim (implemented for OpenDaylight, ONOS and Ryu) and Backend (implemented for Ryu and Floodlight), plus some utilities for testing the Network Engine.

[1] R. Doriguzzi-Corin, E. Salvadori, P. A. A. Gutiérrez, C. Stritzke,
A. Leckey, K. Phemius, E. Rojas, and C. Guerrero, “*NetIDE: Removing
vendor lock-in in SDN*,” in Network Softwarization (NetSoft), 2015 1st
IEEE Conference on, 2015.

![Alt text](/NetIDE-architecture.png?raw=true " ")


The Network Engine in action (from the *NetIDE Project* Youtube channel):

<a href="http://www.youtube.com/watch?feature=player_embedded&v=LnWXqXyoEEk
" target="_blank"><img src="http://img.youtube.com/vi/LnWXqXyoEEk/0.jpg"
alt="IMAGE ALT TEXT HERE" width="480" height="320" border="10" /></a>
