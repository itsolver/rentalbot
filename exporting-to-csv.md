from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter
#CSV importer
class CSVRealstateItemExporter(CsvItemExporter):
    def __init__(self, *args, **kwargs):
    	#kwargs['delimiter'] = settings.get('CSV_DELIMITER', ',')
        # kwargs['fields_to_export'] = settings.getlist('EXPORT_FIELDS') or None
        kwargs['fields_to_export'] = ["url", "property_num", "rent_amount", "bond_amount", "street_address", "suburb", "postcode", "num_bedrooms", "num_bathrooms", "num_carspaces", "property_type", "description", "keywords", "date_available", "allowances", "other_features" ]
        kwargs['encoding'] = settings.get('EXPORT_ENCODING', 'utf-8')
        super(CSVRealstateItemExporter, self).__init__(*args, **kwargs)
