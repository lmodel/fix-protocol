package example;

/* metamodel_version: 1.12.0 */
/* version: FIX.Latest_EP312 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A FIX message, known by its MsgType, such as D for NewOrderSingle, with its members in order.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FixMessage extends FixElement {

  private String abbrName;
  private FixCategory inCategory;
  private List<FixMember> fixMembers;
  private Boolean fixmlNotRequired;
  private String msgType;


}