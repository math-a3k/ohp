.. _ucum_units:

==========
UCUM Units
==========

``ohp`` uses `UCUM units <https://ucum.org/ucum>`_ for measurements.

A ``django-admin`` command, ``import_ucum_units``, is provided to conveniently load and remove the units maintained by UCUM::

	> python manage.py import_ucum_units

To safely remove all units, use the ``--remove`` option, i.e.::

	> python manage.py import_ucum_units --remove
