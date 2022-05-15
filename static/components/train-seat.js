class Train_Seats extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        let trainID = this.getAttribute('trainID');
        this.innerHTML = `<div class="train">
        <ol>
            <li>
                <ol class="seats">
                    <li class="seat">
                        <input type="radio" id="${trainID}-1A" name="seat" value="${trainID}-1A" form="reserve" />
                        <label for="${trainID}-1A">1A</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-1B" name="seat" value="${trainID}-1B" form="reserve" />
                        <label for="${trainID}-1B">1B</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-1C" name="seat" value="${trainID}-1C" form="reserve" />
                        <label for="${trainID}-1C">1C</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-1D" name="seat" value="${trainID}-1D" form="reserve" />
                        <label for="${trainID}-1D">1D</label>
                    </li>
                </ol>
            </li>
            <li>
                <ol class="seats">
                    <li class="seat">
                        <input type="radio" id="${trainID}-2A" name="seat" value="${trainID}-2A" form="reserve" />
                        <label for="${trainID}-2A">2A</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-2B" name="seat" value="${trainID}-2B" form="reserve" />
                        <label for="${trainID}-2B">2B</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-2C" name="seat" value="${trainID}-2C" form="reserve" />
                        <label for="${trainID}-2C">2C</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-2D" name="seat" value="${trainID}-2D" form="reserve" />
                        <label for="${trainID}-2D">2D</label>
                    </li>
                </ol>
            </li>
            <li>
                <ol class="seats">
                    <li class="seat">
                        <input type="radio" id="${trainID}-3A" name="seat" value="${trainID}-3A" form="reserve" />
                        <label for="${trainID}-3A">3A</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-3B" name="seat" value="${trainID}-3B" form="reserve" />
                        <label for="${trainID}-3B">3B</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-3C" name="seat" value="${trainID}-3C" form="reserve" />
                        <label for="${trainID}-3C">3C</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-3D" name="seat" value="${trainID}-3D" form="reserve" />
                        <label for="${trainID}-3D">3D</label>
                    </li>
                </ol>
            </li>
            <li>
                <ol class="seats">
                    <li class="seat">
                        <input type="radio" id="${trainID}-4A" name="seat" value="${trainID}-4A" form="reserve" />
                        <label for="${trainID}-4A">4A</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-4B" name="seat" value="${trainID}-4B" form="reserve" />
                        <label for="${trainID}-4B">4B</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-4C" name="seat" value="${trainID}-4C" form="reserve" />
                        <label for="${trainID}-4C">4C</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-4D" name="seat" value="${trainID}-4D" form="reserve" />
                        <label for="${trainID}-4D">4D</label>
                    </li>
                </ol>
            </li>
            <li>
                <ol class="seats">
                    <li class="seat">
                        <input type="radio" id="${trainID}-5A" name="seat" value="${trainID}-5A"  form="reserve" />
                        <label for="${trainID}-5A">5A</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-5B" name="seat" value="${trainID}-5B" form="reserve" />
                        <label for="${trainID}-5B">5B</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-5C" name="seat" value="${trainID}-5C" form="reserve" />
                        <label for="${trainID}-5C">5C</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-5D" name="seat" value="${trainID}-5D" form="reserve" />
                        <label for="${trainID}-5D">5D</label>
                    </li>
                </ol>
            </li>
            <li>
                <ol class="seats">
                    <li class="seat">
                        <input type="radio" id="${trainID}-6A" name="seat" value="${trainID}-6A" form="reserve" />
                        <label for="${trainID}-6A">6A</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-6B" name="seat" value="${trainID}-6B" form="reserve" />
                        <label for="${trainID}-6B">6B</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-6C" name="seat" value="${trainID}-6C" form="reserve" />
                        <label for="${trainID}-6C">6C</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-6D" name="seat" value="${trainID}-6D" form="reserve" />
                        <label for="${trainID}-6D">6D</label>
                    </li>
                </ol>
            </li>
            <li>
                <ol class="seats">
                    <li class="seat">
                        <input type="radio" id="${trainID}-7A" name="seat" value="${trainID}-7A" form="reserve" />
                        <label for="${trainID}-7A">7A</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-7B" name="seat" value="${trainID}-7B" form="reserve" />
                        <label for="${trainID}-7B">7B</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-7C" name="seat" value="${trainID}-7C" form="reserve" />
                        <label for="${trainID}-7C">7C</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-7D" name="seat" value="${trainID}-7D" form="reserve" />
                        <label for="${trainID}-7D">7D</label>
                    </li>
                </ol>
            </li>
            <li>
                <ol class="seats">
                    <li class="seat">
                        <input type="radio" id="${trainID}-8A" name="seat" value="${trainID}-8A" form="reserve" />
                        <label for="${trainID}-8A">8A</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-8B" name="seat" value="${trainID}-8B" form="reserve" />
                        <label for="${trainID}-8B">8B</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-8C" name="seat" value="${trainID}-8C" form="reserve" />
                        <label for="${trainID}-8C">8C</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-8D" name="seat" value="${trainID}-8D" form="reserve" />
                        <label for="${trainID}-8D">8D</label>
                    </li>
                </ol>
            </li>
            <li>
                <ol class="seats">
                    <li class="seat">
                        <input type="radio" id="${trainID}-9A" name="seat" value="${trainID}-9A" form="reserve" />
                        <label for="${trainID}-9A">9A</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-9B" name="seat" value="${trainID}-9B" form="reserve" />
                        <label for="${trainID}-9B">9B</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-9C" name="seat" value="${trainID}-9C" form="reserve" />
                        <label for="${trainID}-9C">9C</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-9D" name="seat" value="${trainID}-9D" form="reserve" />
                        <label for="${trainID}-9D">9D</label>
                    </li>
                </ol>
            </li>
            <li>
                <ol class="seats">
                    <li class="seat">
                        <input type="radio" id="${trainID}-10A" name="seat" value="${trainID}-10A" form="reserve" />
                        <label for="${trainID}-10A">10A</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-10B" name="seat" value="${trainID}-10B" form="reserve" />
                        <label for="${trainID}-10B">10B</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-10C" name="seat" value="${trainID}-10C" form="reserve" />
                        <label for="${trainID}-10C">10C</label>
                    </li>
                    <li class="seat">
                        <input type="radio" id="${trainID}-10D" name="seat" value="${trainID}-10D" form="reserve" />
                        <label for="${trainID}-10D">10D</label>
                    </li>
                </ol>
            </li>
        </ol>
    </div>`;

        let _list = this.getAttribute("dis");
        if (_list) {
            _list.split(" ").forEach(id => {
                document.getElementById(id).setAttribute("disabled", true);
            });
        }
    }
}

customElements.define('train-seats', Train_Seats);