# -------------------------------------------------------------------------------
# Copyright IBM Corp. 2017
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------------

from pixiedust.display.chart.renderers import PixiedustRenderer
from .matplotlibBaseDisplay import MatplotlibBaseDisplay
from pixiedust.display.chart.renderers.colors import Colors

@PixiedustRenderer(id="scatterPlot")
class ScatterPlotDisplay(MatplotlibBaseDisplay):
    
	def supportsAggregation(self, handlerId):
		return False

	def supportsLegend(self, handlerId):
		return False
    
	def canRenderChart(self):
		valueFields = self.getValueFields()
		if len(valueFields) != 1:
			return (False, "Can only specify one Value Field")

		#Verify that all key field are numericals
		for keyField in self.getKeyFields():
			if not self.dataHandler.isNumericField(keyField):
				return (False, "Column {0} is not numerical".format(keyField))
		
		return (True, None)

	def getPreferredDefaultValueFieldCount(self, handlerId):
		return 2

	def matplotlibRender(self, fig, ax):
		keyFields = self.getKeyFields()
		for i,keyField in enumerate(keyFields):
			self.getWorkingPandasDataFrame().plot(kind='scatter', x=keyField, y=self.getValueFields()[0], 
				label=keyField, ax=ax, color=Colors[1.*i/len(keyFields)], figsize=(8, 8))