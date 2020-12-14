from flask import render_template, redirect, url_for, request
from flask_login import login_required
import os
from werkzeug.urls import url_parse
from flask_login import login_user, logout_user, current_user
from app.iqa import bp
from app.iqa.forms import DataForm


@bp.route('/groups', methods=['GET'])
@login_required
def groups():
	card_set = []
	for row_index in range(9):
		group_info = []
		for i in range(3):
			group_info.append({
				'group_url': url_for('iqa.iqa', group_name=3*row_index+i),
				'group_cover': url_for('static', filename="group_covers/"+str(3*row_index+i)+".jpg"),
				'group_id': "Group "+str(3*row_index+i)})
		card_set.append(group_info)
	return render_template('iqa/groups.html', card_set=card_set)


@bp.route('/iqa/?<string:group_name>', methods=['GET', 'POST'])
@login_required
def iqa(group_name):
	image_file_list = os.listdir("./app" + url_for('static', filename=group_name))
	print(type(group_name))
	print("THE:")
	print(group_name)
	if group_name == "27":
		max_len = 15
	else:
		max_len = 30
	print(max_len)
	img_file_names = []
	for img in image_file_list:
		img_file_names.append(url_for('static', filename=group_name+"/"+img))
	form = DataForm()
	iqa_items = form.build_dict(img_file_names)
	iqa_items_short = [
		{'filename': img_file_names[0], 'slider': form.get_slider_list()[0]},
		{'filename': img_file_names[1], 'slider': form.get_slider_list()[1]},
		{'filename': img_file_names[2], 'slider': form.get_slider_list()[2]}]
	if current_user.is_authenticated:
		print(current_user)
	if form.validate_on_submit():
		filename = "./app/data/"+str(current_user).strip('<>')+group_name+".txt"
		data_file = open(filename, "a+")
		for i in range(max_len):
			data_file.write(image_file_list[i]+"\t"+str(form.get_slider_list()[i].data)+"\n")
		data_file.close()
		return redirect(url_for('iqa.groups'))
		
	return render_template('iqa/iqa.html', title='iqa', iqa_items=iqa_items[:max_len], form=form)

