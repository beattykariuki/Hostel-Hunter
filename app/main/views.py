from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Review
import markdown2
from .forms import ReviewForm
from .. import db,photos
from datetime import datetime
from flask_login import login_required,current_user


@main.route("/<user>/hostel/<hostel_id>/add-review", methods = ["GET","POST"])
@login_required
def review(user,review_id):
    user = User.query.filter_by(id = user).first()
    review = Review.query.filter_by(id = _id).first()
    form = ReviewForm()
    title = "Add review"
    if form.validate_on_submit():
        content = form.comment.data 
        posted = datetime.now()
        new_review = Review(user = user,review = form.review.data,posted = posted)
        new_review.save_comment()
    #     return redirect(url_for("main.view_comments", pitch_id=pitch.id))
    # return render_template("/new_comment.html", title = pitch.title,form = form,pitch = pitch)
