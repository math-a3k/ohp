.. _loinc_codes:

==========
UCUM Units
==========

``ohp`` uses `LOINC codes <https://ucum.org/ucum>`_.

A ``django-admin`` command, ``import_loinc_codes``, is provided to conveniently load and remove the codes::

	> python manage.py import_loinc_codes

To safely remove all units, use the ``--remove`` option, i.e.::

	> python manage.py import_loinc_codes --remove


The setting ``OHP_LOINC_ZIP_FILE`` controls which file is to be loaded. A stripped versoin of the LOINC codes is included in the codebase - with the corresponding license - for convenience.
