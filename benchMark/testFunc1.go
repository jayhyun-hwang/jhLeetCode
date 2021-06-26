package benchMark

var Case1 = "SVWEASVAVASDFVXZC"
var Case2 = "Avrvavavavbeadvsdv"
var Case3 = "fdbadrgabeatasvasbfa"
var Case4 = "avasdvASDfvasdASDVaewgsavaSDVasdv"

func testFunc1() {
	// fmt.Println(testFunc11(Case1))
	// fmt.Println(testFunc11(Case2))
	// fmt.Println(testFunc11(Case3))
	// fmt.Println(testFunc11(Case4))
	testFunc11(Case1)
	testFunc11(Case2)
	testFunc11(Case3)
	testFunc11(Case4)
}
func testFunc11(word string) bool {
	if len(word) == 1 {
		return true
	}
	var firstIsUp bool
	if word[0] < 91 {
		firstIsUp = true
	} else {
		firstIsUp = false
	}
	obj := new(Obj)
	obj.word = word
	if word[1] < 91 {
		obj.shouldUpper = true
	} else {
		obj.shouldUpper = false
	}
	if !firstIsUp && obj.shouldUpper {
		return false
	}
	var piv byte
	if obj.shouldUpper {
		piv = 64
	} else {
		piv = 96
	}
	obj.idx = 2
	return obj.findSol(piv)
}

type Obj struct {
	word        string
	idx         int
	shouldUpper bool
}

func (obj *Obj) findSol(piv byte) bool {
	if obj.idx >= len(obj.word) {
		return true
	}
	if obj.word[obj.idx] > piv && obj.word[obj.idx] < piv+27 {
		obj.idx++
		return obj.findSol(piv)
	}
	return false
}
