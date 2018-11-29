from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from flask_login import UserMixin
from ..models import Reviews,User
from .forms import ReviewForm,UpdateProfile
from ..import db,photos

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data 

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

        return render_template("profile/update.html", form = form)

@main.route('/hostel/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    form = ReviewForm()
    hostel = get_hostel(id)
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        #update review instance
        new_review = Review(hostel_id=hostel.id,hostel_title=title,image_path=hostel.poster,hostel_review=review,user=current_user)

        #save review method
        new_review.save_review()
        return redirect(url_for('.hostel',id = hostel.id))

    title = f'{movie.title} review'
    return redirect(url_for('.new_review.html',title = title, review_form=form, movie=movie))
        

