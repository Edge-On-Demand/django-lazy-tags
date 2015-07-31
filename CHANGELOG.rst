Changelog
=========

* 0.2.1 (July 31, 2015)
    * Fixed issue where templates were not on PyPI.

* 0.2.0 (July 30, 2015)
    * Use Django cache instead of URL parameters in order to prevent potential remote code execution.
    * Fixed issue where tags with multiple args would not work.
    * Removed template tag args/kwargs always being passed in as strings.
    * Removed LAZY_TAGS_FORCE_LOGIN setting. Not needed now that remote code execution issue is fixed.

* 0.1 (July 28, 2015)
    * Initial alpha release