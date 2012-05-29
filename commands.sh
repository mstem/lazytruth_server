alias lazytruth-down="rsync -av --exclude 'media*' --exclude 'static*' --exclude '*.pyc' stefan@lazytruth.media.mit.edu:/var/stem/lazytruth/ /var/ion/lazytruth/"
alias lazytruth-up="rsync -av --exclude 'media*' --exclude 'static*' --exclude '*.pyc' /var/ion/lazytruth/ stefan@lazytruth.media.mit.edu:/var/stem/lazytruth/"
alias lazytruth-cleandb="cd /var/stem/lazytruth && rm apps/data/migrations/0001* && python manage.py schemamigration data --initial && sudo -u postgres psql < initdb.sql && python manage.py syncdb && python manage.py migrate data"
alias lazytruth-solr-schema="cd /var/stem/lazytruth && python manage.py build_solr_schema > ../apache-solr-3.5.0/example/solr/conf/schema.xml"