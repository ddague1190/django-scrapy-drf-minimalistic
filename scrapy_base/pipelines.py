from itemadapter import ItemAdapter
from django_app.models import Bike, Manufacturer



class ScrapyBasePipeline:
    def years_made(self, range):
        years = range.split('-')
        return years if len(years)==2 else years+years

    def process_item(self, item, spider):
        mfg, _ = Manufacturer.objects.get_or_create(name=item.get('mfg'))
        [start, end] = self.years_made(item.get('years_made'))
        model = item.get('model')
        bike = Bike(
            model=model, 
            mfg = mfg,
            start_year=start,
            end_year=end
        )
        bike.save()
        return item
    