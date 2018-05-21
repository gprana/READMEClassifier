# NAME

GeoIP2 - Perl API for MaxMind's GeoIP2 web services and databases

# VERSION

version 2.003001

# DESCRIPTION

This distribution provides an API for the GeoIP2
[web services](http://dev.maxmind.com/geoip/geoip2/web-services) and
[databases](http://dev.maxmind.com/geoip/geoip2/downloadable). The API also
works with the free
[GeoLite2 databases](http://dev.maxmind.com/geoip/geoip2/geolite2/).

See [GeoIP2::WebService::Client](https://metacpan.org/pod/GeoIP2::WebService::Client) for details on the web service client API
and [GeoIP2::Database::Reader](https://metacpan.org/pod/GeoIP2::Database::Reader) for the database API.

# SPEEDING UP DATABASE READING

This module only depends on the pure Perl implementation of the MaxMind
database reader ([MaxMind::DB::Reader](https://metacpan.org/pod/MaxMind::DB::Reader)). If you install the libmaxminddb
library ([http://maxmind.github.io/libmaxminddb/](http://maxmind.github.io/libmaxminddb/)) and
[MaxMind::DB::Reader::XS](https://metacpan.org/pod/MaxMind::DB::Reader::XS), then the XS implementation will be loaded
automatically. The XS implementation is approximately 100x faster than the
pure Perl implementation.

# VALUES TO USE FOR DATABASE OR HASH KEYS

**We strongly discourage you from using a value from any `names` accessor as
a key in a database or hash.**

These names may change between releases. Instead we recommend using one of the
following:

- [GeoIP2::Record::City](https://metacpan.org/pod/GeoIP2::Record::City) - `$city->geoname_id`
- [GeoIP2::Record::Continent](https://metacpan.org/pod/GeoIP2::Record::Continent) - `$continent->code` or `$continent->geoname_id`
- [GeoIP2::Record::Country](https://metacpan.org/pod/GeoIP2::Record::Country) and [GeoIP2::Record::RepresentedCountry](https://metacpan.org/pod/GeoIP2::Record::RepresentedCountry) - `$country->iso_code` or `$country->geoname_id`
- [GeoIP2::Record::Subdivision](https://metacpan.org/pod/GeoIP2::Record::Subdivision) - `$subdivision->iso_code` or `$subdivision->geoname_id`

# INTEGRATION WITH GEONAMES

GeoNames ([http://www.geonames.org/](http://www.geonames.org/)) offers web services and downloadable
databases with data on geographical features around the world, including
populated places. They offer both free and paid premium data. Each feature is
uniquely identified by a `geoname_id`, which is an integer.

Many of the records returned by the GeoIP web services and databases include a
`geoname_id` field. This is the ID of a geographical feature (city, region,
country, etc.) in the GeoNames database.

Some of the data that MaxMind provides is also sourced from GeoNames. We
source data such as place names, ISO codes, and other similar data from the
GeoNames premium data set.

# REPORTING DATA PROBLEMS

If the problem you find is that an IP address is incorrectly mapped, please
submit your correction to MaxMind at [http://www.maxmind.com/en/correction](http://www.maxmind.com/en/correction).

If you find some other sort of mistake, like an incorrect spelling, please
check the GeoNames site ([http://www.geonames.org/](http://www.geonames.org/)) first. Once you've searched
for a place and found it on the GeoNames map view, there are a number of links
you can use to correct data ("move", "edit", "alternate names", etc.). Once
the correction is part of the GeoNames data set, it will be automatically
incorporated into future MaxMind releases.

If you are a paying MaxMind customer and you're not sure where to submit a
correction, please contact MaxMind support at for help. See
[http://www.maxmind.com/en/support](http://www.maxmind.com/en/support) for support details.

# VERSIONING POLICY

This module uses semantic versioning as described by
[http://semver.org/](http://semver.org/). Version numbers can be read as X.YYYZZZ, where X is the
major number, YYY is the minor number, and ZZZ is the patch number.

# PERL VERSION SUPPORT

MaxMind has tested this API with Perl 5.8.8 and above. Reasonable patches for
earlier versions of Perl 5.8 will be applied. We will not accept patches to
support any version of Perl before 5.8.

The data returned from the GeoIP2 web services includes Unicode characters in
several locales. This may expose bugs in earlier versions of Perl. If Unicode
support is important to you, we recommend that you use the most recent version
of Perl available.

# SUPPORT

Please report all issues with this code using the GitHub issue tracker at
[https://github.com/maxmind/GeoIP2-perl/issues](https://github.com/maxmind/GeoIP2-perl/issues).

If you are having an issue with a MaxMind service that is not specific to the
client API please see [http://www.maxmind.com/en/support](http://www.maxmind.com/en/support) for details.

# AUTHORS

- Dave Rolsky &lt;drolsky@maxmind.com>
- Greg Oschwald &lt;goschwald@maxmind.com>
- Mark Fowler &lt;mfowler@maxmind.com>
- Olaf Alders &lt;oalders@maxmind.com>

# CONTRIBUTORS

- Andy Jack &lt;github@veracity.ca>
- E. Choroba &lt;choroba@matfyz.cz>
- Graham Knop &lt;haarg@haarg.org>
- Mateu X Hunter &lt;mhunter@maxmind.com>

# COPYRIGHT AND LICENSE

This software is copyright (c) 2013 - 2016 by MaxMind, Inc.

This is free software; you can redistribute it and/or modify it under
the same terms as the Perl 5 programming language system itself.
