from matplotlib import pyplot

import impl_1
import impl_2
import impl_3


pyplot.xlabel('N, search range')
pyplot.ylabel('Time, seconds')
pyplot.plot(*impl_1.test(), label=impl_1.__name__)
pyplot.plot(*impl_2.test(), label=impl_2.__name__)
pyplot.plot(*impl_3.test(), label=impl_3.__name__)
pyplot.legend()
pyplot.show()
