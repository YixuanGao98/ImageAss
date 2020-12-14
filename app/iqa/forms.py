from flask_wtf import FlaskForm
from wtforms import Form, SubmitField
from wtforms.fields.html5 import DecimalRangeField
from wtforms.validators import NumberRange


class DataForm(FlaskForm):
	val1 = DecimalRangeField('val1', default=0, validators=[NumberRange(min=0, max=100)])
	val2 = DecimalRangeField('val2', default=0, validators=[NumberRange(min=0, max=100)])
	val3 = DecimalRangeField('val3', default=0, validators=[NumberRange(min=0, max=100)])
	val4 = DecimalRangeField('val4', default=0, validators=[NumberRange(min=0, max=100)])
	val5 = DecimalRangeField('val1', default=0, validators=[NumberRange(min=0, max=100)])
	val6 = DecimalRangeField('val2', default=0, validators=[NumberRange(min=0, max=100)])
	val7 = DecimalRangeField('val3', default=0, validators=[NumberRange(min=0, max=100)])
	val8 = DecimalRangeField('val4', default=0, validators=[NumberRange(min=0, max=100)])
	val9 = DecimalRangeField('val1', default=0, validators=[NumberRange(min=0, max=100)])
	val10 = DecimalRangeField('val2', default=0, validators=[NumberRange(min=0, max=100)])
	val11 = DecimalRangeField('val3', default=0, validators=[NumberRange(min=0, max=100)])
	val12 = DecimalRangeField('val4', default=0, validators=[NumberRange(min=0, max=100)])
	val13 = DecimalRangeField('val1', default=0, validators=[NumberRange(min=0, max=100)])
	val14 = DecimalRangeField('val2', default=0, validators=[NumberRange(min=0, max=100)])
	val15 = DecimalRangeField('val3', default=0, validators=[NumberRange(min=0, max=100)])
	val16 = DecimalRangeField('val4', default=0, validators=[NumberRange(min=0, max=100)])
	val17 = DecimalRangeField('val1', default=0, validators=[NumberRange(min=0, max=100)])
	val18 = DecimalRangeField('val2', default=0, validators=[NumberRange(min=0, max=100)])
	val19 = DecimalRangeField('val3', default=0, validators=[NumberRange(min=0, max=100)])
	val20 = DecimalRangeField('val4', default=0, validators=[NumberRange(min=0, max=100)])
	val21 = DecimalRangeField('val1', default=0, validators=[NumberRange(min=0, max=100)])
	val22 = DecimalRangeField('val2', default=0, validators=[NumberRange(min=0, max=100)])
	val23 = DecimalRangeField('val3', default=0, validators=[NumberRange(min=0, max=100)])
	val24 = DecimalRangeField('val4', default=0, validators=[NumberRange(min=0, max=100)])
	val25 = DecimalRangeField('val1', default=0, validators=[NumberRange(min=0, max=100)])
	val26 = DecimalRangeField('val2', default=0, validators=[NumberRange(min=0, max=100)])
	val27 = DecimalRangeField('val3', default=0, validators=[NumberRange(min=0, max=100)])
	val28 = DecimalRangeField('val4', default=0, validators=[NumberRange(min=0, max=100)])
	val29 = DecimalRangeField('val1', default=0, validators=[NumberRange(min=0, max=100)])
	val30 = DecimalRangeField('val2', default=0, validators=[NumberRange(min=0, max=100)])

	def build_dict(self, filenames):
		iqa_list = []
		slider_list = self.get_slider_list()
		for i in range(len(filenames)):
			iqa_list.append({'filename': filenames[i], 'slider': slider_list[i]})
		return iqa_list
	
	def get_slider_list(self):
		return [
			self.val1, self.val2, self.val3, self.val4, self.val5, self.val6,
			self.val7, self.val8, self.val9, self.val10, self.val11, self.val2,
			self.val13, self.val14, self.val15, self.val16, self.val17, self.val18,
			self.val19, self.val20, self.val21, self.val22, self.val23, self.val24,
			self.val25, self.val26, self.val27, self.val28, self.val29, self.val30]
	
	def get_data_list(self):
		return [self.val1.data, self.val2.data, self.val3.data, self.val4.data]
	submit = SubmitField('Submit')
