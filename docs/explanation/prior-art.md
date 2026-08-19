# Relationship to MMStudio & prior art

`pymmcore-gui` aims to be a pure-Python replacement for the traditional
Java-based Micro-Manager GUI ([MMStudio, and its
plugins](https://github.com/micro-manager/micro-manager)). The interface is
meant to feel familiar to existing Micro-Manager users, while being more
flexible, modern, and user-extensible — benefiting from the Python
ecosystem instead of requiring Java.

## Why not MMStudio?

MMStudio talks to the same underlying C++ core (`MMCore`) that
`pymmcore-plus` does, but it's written in Java, with plugins in Java and
Clojure. That makes it hard to extend from Python, and means keeping a JVM
in the loop. `pymmcore-gui` re-implements the GUI layer natively in Python,
so device control, acquisition, and any custom analysis/processing code can
live in the same process and language.

## Prior projects this builds on

- [**napari-micromanager**](https://github.com/pymmcore-plus/napari-micromanager) —
  a plugin using napari as the viewer and `pymmcore-widgets` for UI. It
  demonstrated Micro-Manager control in a Python GUI, and remains usable for
  those who prefer a napari-based workflow, though it's no longer under
  active development.
- [**micromanager-gui**](https://github.com/fdrgsp/micromanager-gui) by
  Federico Gasparoli.
- [**pymmcore-plus-sandbox**](https://github.com/gselzer/pymmcore-plus-sandbox)
  by Gabe Selzer.

Lessons from these prototypes (and others, e.g. at LEB-EPFL) shaped
`pymmcore-gui`'s design — including one prototype's approach of mimicking
the MMStudio layout directly. By unifying ideas from these efforts,
`pymmcore-gui` aims to be a single, officially-supported application for the
pymmcore-plus ecosystem, rather than another one-off GUI.

## How this differs from Pycro-Manager

See the "How is pymmcore-plus different than Pycro-Manager?" note on the
[pymmcore-plus overview page](https://pymmcore-plus.github.io/pymmcore-plus/) —
the same distinction applies here: Pycro-Manager drives Micro-Manager
through a running Java MMStudio process over ZMQ, whereas `pymmcore-gui`
(via `pymmcore-plus`) talks to the C++ core directly, with no Java process
involved.
