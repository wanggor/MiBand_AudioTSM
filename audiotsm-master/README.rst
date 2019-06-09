A real-time audio time-scale modification library
=================================================

.. image:: https://readthedocs.org/projects/audiotsm/badge/?version=latest
    :target: http://audiotsm.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://travis-ci.org/Muges/audiotsm.svg?branch=master
    :target: https://travis-ci.org/Muges/audiotsm
    :alt: Build Status

AudioTSM is a python library for real-time audio time-scale modification
procedures, i.e. algorithms that change the speed of an audio signal without
changing its pitch.

Documentation:
   https://audiotsm.readthedocs.io/

Examples:
    https://muges.github.io/audiotsm/

Source code repository and issue tracker:
   https://github.com/Muges/audiotsm/

Python Package Index:
    https://pypi.python.org/pypi/audiotsm/

License:
   MIT -- see the file ``LICENSE`` for details.

Installation
------------

Audiotsm should work with python 2.7 and python 3.4+.

You can install the latest version of audiotsm with pip::

    pip install audiotsm

If you want to use the gstreamer plugins, you should install PyGObject_ and
python-gst_, and use the following command to install audiotsm::

    pip install audiotsm[gstreamer]

If you want to play the output of the TSM procedures in real time, or to use
the examples, you should install audiotsm as follow::

    pip install audiotsm[stream]

.. _PyGObject:
    https://pygobject.readthedocs.io/en/latest/getting_started.html

.. _python-gst:
    https://gstreamer.freedesktop.org/modules/gst-python.html


Basic usage
-----------

The audiotsm package implements several time-scale modification procedures:

- OLA (Overlap-Add);
- WSOLA (Waveform Similarity-based Overlap-Add);
- Phase Vocoder.

The OLA procedure should only be used on percussive audio signals. The WSOLA
and the Phase Vocoder procedures are improvements of the OLA procedure, and
should both give good results in most cases.

If you are unsure which procedure to choose, the Phase Vocoder should sound
best in most cases. You can listen to the output of the different procedures on
various audio files and at various speeds on the `examples page`_.

.. _examples page: https://muges.github.io/audiotsm/

Python API
~~~~~~~~~~

Below is a basic example showing how to reduce the speed of a wav file by half
using the phase vocoder procedure::

    from audiotsm import phasevocoder
    from audiotsm.io.wav import WavReader, WavWriter

    with WavReader(input_filename) as reader:
        with WavWriter(output_filename, reader.channels, reader.samplerate) as writer:
            tsm = phasevocoder(reader.channels, speed=0.5)
            tsm.run(reader, writer)

A complete example can be found in the ``examples/audiotsmcli.py`` file. Read
the documentation__ for more details.

__ http://audiotsm.readthedocs.io/en/latest/tsm.html

GStreamer plugins
~~~~~~~~~~~~~~~~~

The TSM procedures are also available as GStreamer plugins. A simple example
implementing a basic GStreamer pipeline can be found in the
``examples/audiotsmcli_gst.py`` file, and a more complete one showing how to
use the plugins in a GTK audio player can be found in the
``examples/audiotsmgtk.py`` file. Read the documentation__ for more details.

__ http://audiotsm.readthedocs.io/en/latest/gstreamer.html

Thanks
------

If you are interested in time-scale modification procedures, I highly recommend
reading `A Review of Time-Scale Modification of Music Signals`_ by Jonathan
Driedger and Meinard Müller.

.. _A Review of Time-Scale Modification of Music Signals:
    http://www.mdpi.com/2076-3417/6/2/57
