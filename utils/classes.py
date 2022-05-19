from utils import get_posts_all


class Messages:
    def __init__(self, poster_name, poster_avatar, pic, content, views_count, likes_count, pk):
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count
        self.pk = pk

    def __repr__(self):
        return str(self.pk)


class Comment:
    def __init__(self, post_id, commenter_name, comment, pk):
        self.post_id = post_id
        self.commenter_name = commenter_name
        self.comment = comment
        self.pk = pk


messages_raw_db = get_posts_all()
messages_db = []

for line in messages_raw_db:
    messages_db.append(
        Messages(
            poster_name=line['poster_name'],
            poster_avatar=line['poster_avatar'],
            pic=line['pic'],
            content=line['content'],
            views_count=line['views_count'],
            likes_count=line['likes_count'],
            pk=line['pk']
        )
    )

print(messages_db)
