class Cats:
    def get_fat_cat(cat_list):
        fat_cat = cat_list[0]
        for cat in cat_list:
            if fat_cat.get_weight() < cat.get_weight():
                fat_cat = cat
        return fat_cat

    def get_old_cat(cat_list):
        pass

    def get_from_old_cats_fat(cat_list):
        pass