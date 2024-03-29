from flask import render_template, request, Blueprint
from flaskblog.models import Post
from flaskblog.requests import get_quotes

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")

def about():  
    quotes = get_quotes()
    return render_template('about.html', title='About', quotes=quotes)
